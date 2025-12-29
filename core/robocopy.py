"""
FastCopy - Robocopy Wrapper v1.4
Python interface for Windows Robocopy with real-time progress.
"""
import subprocess
import threading
import os
from typing import Generator, Optional, Callable, List
from dataclasses import dataclass, field
from enum import Enum
from .parser import RobocopyParser, ProgressInfo, CopyStatus, CopyStatistics


class CopyMode(Enum):
    """Copy operation mode"""
    COPY = "copy"
    MIRROR = "mirror"
    MOVE = "move"


@dataclass
class CopyOptions:
    """Robocopy options"""
    mode: CopyMode = CopyMode.COPY
    threads: int = 8
    retry_count: int = 3
    retry_wait: int = 5
    copy_subdirs: bool = True
    copy_empty_dirs: bool = True
    include_patterns: List[str] = field(default_factory=list)
    exclude_patterns: List[str] = field(default_factory=list)
    exclude_dirs: List[str] = field(default_factory=list)
    copy_attributes: bool = True
    copy_timestamps: bool = True


class RobocopyRunner:
    """Robocopy wrapper with real-time progress tracking"""
    
    def __init__(self):
        self._process: Optional[subprocess.Popen] = None
        self._parser = RobocopyParser()
        self._running = False
        self._cancelled = False
        self._lock = threading.Lock()
        
    def _build_cmd(self, src: str, dst: str, opts: CopyOptions) -> List[str]:
        """Build robocopy command"""
        cmd = ["robocopy", src, dst]
        
        # Mode
        if opts.mode == CopyMode.MIRROR:
            cmd.append("/MIR")
        elif opts.mode == CopyMode.MOVE:
            cmd.append("/MOVE")
        elif opts.copy_subdirs:
            cmd.append("/E" if opts.copy_empty_dirs else "/S")
            
        # Threading
        if opts.threads > 1:
            cmd.append(f"/MT:{min(opts.threads, 128)}")
            
        # Retry
        cmd.extend([f"/R:{opts.retry_count}", f"/W:{opts.retry_wait}"])
        
        # Attributes
        if opts.copy_attributes and opts.copy_timestamps:
            cmd.append("/COPY:DAT")
            
        # Patterns
        cmd.extend(opts.include_patterns)
        if opts.exclude_patterns:
            cmd.extend(["/XF"] + opts.exclude_patterns)
        if opts.exclude_dirs:
            cmd.extend(["/XD"] + opts.exclude_dirs)
            
        # Output format (no /NP to get progress %)
        cmd.append("/BYTES")
        
        return cmd
        
    def set_totals(self, total_bytes: int, total_files: int):
        """Set pre-calculated totals"""
        self._parser.set_totals(total_bytes, total_files)
        
    def copy(
        self, src: str, dst: str,
        opts: Optional[CopyOptions] = None,
        callback: Optional[Callable[[ProgressInfo], None]] = None
    ) -> Generator[ProgressInfo, None, CopyStatistics]:
        """Run copy operation with progress"""
        return self._run(src, dst, opts or CopyOptions(), callback)
        
    def _run(
        self, src: str, dst: str, opts: CopyOptions,
        callback: Optional[Callable[[ProgressInfo], None]] = None
    ) -> Generator[ProgressInfo, None, CopyStatistics]:
        """Execute robocopy"""
        with self._lock:
            if self._running:
                raise RuntimeError("Already running")
            self._running = True
            self._cancelled = False
            
        self._parser.reset()
        cmd = self._build_cmd(src, dst, opts)
        
        try:
            self._process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding='utf-8',
                errors='replace',
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0,
                bufsize=1
            )
            
            self._parser.progress.status = CopyStatus.RUNNING
            
            for line in iter(self._process.stdout.readline, ''):
                if self._cancelled:
                    self._parser.progress.status = CopyStatus.CANCELLED
                    break
                    
                progress = self._parser.parse_line(line)
                if callback:
                    callback(progress)
                yield progress
                    
            self._process.wait()
            
            # Final status
            if self._cancelled:
                self._parser.progress.status = CopyStatus.CANCELLED
            elif self._process.returncode >= 8:
                self._parser.progress.status = CopyStatus.FAILED
            else:
                self._parser.progress.status = CopyStatus.COMPLETED
                self._parser.progress.percent = 100.0
                
            final = self._parser.get_progress()
            if callback:
                callback(final)
            yield final
            
        except Exception as e:
            self._parser.progress.status = CopyStatus.FAILED
            self._parser.progress.errors.append(str(e))
            yield self._parser.get_progress()
            
        finally:
            with self._lock:
                self._running = False
                self._process = None
                
        return self._parser.get_statistics()
        
    def cancel(self):
        """Cancel operation"""
        with self._lock:
            self._cancelled = True
            if self._process:
                try:
                    self._process.terminate()
                except OSError:
                    pass
                    
    def is_running(self) -> bool:
        with self._lock:
            return self._running
            
    @staticmethod
    def is_available() -> bool:
        """Check if robocopy exists"""
        try:
            subprocess.run(
                ["robocopy", "/?"],
                capture_output=True,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0
            )
            return True
        except FileNotFoundError:
            return False
