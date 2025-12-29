"""
FastCopy - Core Parser Module v1.4
Parses Robocopy output for real-time progress tracking.
"""
import re
from dataclasses import dataclass, field
from typing import List
from enum import Enum


class CopyStatus(Enum):
    """Copy operation status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class ProgressInfo:
    """Real-time progress information"""
    current_file: str = ""
    files_copied: int = 0
    files_total: int = 0
    bytes_copied: int = 0
    bytes_total: int = 0
    percent: float = 0.0
    speed_mbps: float = 0.0
    status: CopyStatus = CopyStatus.PENDING
    current_action: str = ""
    errors: List[str] = field(default_factory=list)
    log_lines: List[str] = field(default_factory=list)


@dataclass 
class CopyStatistics:
    """Final copy statistics"""
    files_total: int = 0
    files_copied: int = 0
    bytes_total: int = 0
    bytes_copied: int = 0


class RobocopyParser:
    """
    Parses Robocopy output for progress tracking.
    
    Handles output patterns:
    - "New File  1234567  filename.txt" - file starting
    - "  45.5%" / "100%" - progress during copy
    - Summary statistics at end
    """
    
    # Compiled regex patterns for performance
    RE_PERCENT = re.compile(r'^\s*(\d+(?:\.\d+)?)\s*%\s*$')
    RE_NEW_FILE = re.compile(r'^\s*(New File|Newer|Older|Changed|same)\s+(\d+)\s+(.+)$', re.I)
    RE_NEW_DIR = re.compile(r'^\s*(New Dir|Extra Dir)\s+\d+\s+(.+)$', re.I)
    RE_FILES = re.compile(r'^\s*Files\s*:\s*(\d+)\s+(\d+)', re.I)
    RE_BYTES = re.compile(r'^\s*Bytes\s*:\s*([\d\.]+\s*[kmgt]?)\s+([\d\.]+\s*[kmgt]?)', re.I)
    RE_SPEED = re.compile(r'Speed\s*:\s*([\d,\.]+)\s*Bytes', re.I)
    
    def __init__(self):
        self._reset_state()
        
    def _reset_state(self):
        """Reset internal state"""
        self.progress = ProgressInfo()
        self.statistics = CopyStatistics()
        self._files_done = 0
        self._bytes_done = 0
        self._cur_file_size = 0
        self._cur_file_pct = 0.0
        self._in_summary = False
        self._total_bytes = 0
        self._total_files = 0
        
    def set_totals(self, total_bytes: int, total_files: int):
        """Set pre-calculated totals"""
        self._total_bytes = total_bytes
        self._total_files = total_files
        self.progress.bytes_total = total_bytes
        self.progress.files_total = total_files
        
    def parse_line(self, line: str) -> ProgressInfo:
        """Parse a line and return updated progress"""
        stripped = line.strip()
        
        # Log non-empty, non-percentage lines
        if stripped and not self.RE_PERCENT.match(stripped):
            if len(self.progress.log_lines) < 300:
                self.progress.log_lines.append(stripped[:80])
        
        if not stripped:
            return self.progress
            
        # Check errors
        if 'ERROR' in stripped.upper():
            self.progress.errors.append(stripped)
            return self.progress
            
        # Check summary section
        if 'Total    Copied' in stripped:
            self._in_summary = True
            
        if self._in_summary:
            self._parse_summary(stripped)
            return self.progress
        
        # Parse percentage (real-time progress)
        m = self.RE_PERCENT.match(stripped)
        if m:
            pct = float(m.group(1))
            self._cur_file_pct = pct
            
            if self._cur_file_size > 0:
                cur_bytes = int(self._cur_file_size * pct / 100)
                self.progress.bytes_copied = self._bytes_done + cur_bytes
                
                if pct >= 100:
                    self._bytes_done += self._cur_file_size
                    self._files_done += 1
                    self.progress.files_copied = self._files_done
                    self._cur_file_size = 0
                    self._cur_file_pct = 0
                    
            self._update_percent()
            return self.progress
            
        # Parse new file
        m = self.RE_NEW_FILE.match(stripped)
        if m:
            action, size, name = m.groups()
            
            # Count previous file if not 100%
            if self._cur_file_size > 0 and self._cur_file_pct < 100:
                self._bytes_done += self._cur_file_size
                self._files_done += 1
                
            self._cur_file_size = int(size)
            self._cur_file_pct = 0
            self.progress.current_file = name.strip()
            self.progress.current_action = action
            self.progress.status = CopyStatus.RUNNING
            self.progress.files_copied = self._files_done
            self.progress.bytes_copied = self._bytes_done
            self._update_percent()
            return self.progress
            
        # Parse directory
        m = self.RE_NEW_DIR.match(stripped)
        if m:
            self.progress.current_action = m.group(1)
            self.progress.current_file = m.group(2).strip()
            
        return self.progress
        
    def _parse_summary(self, line: str):
        """Parse summary statistics"""
        m = self.RE_FILES.match(line)
        if m:
            self.statistics.files_total = int(m.group(1))
            self.statistics.files_copied = int(m.group(2))
            self.progress.files_total = self.statistics.files_total
            self.progress.files_copied = self.statistics.files_copied
            
        m = self.RE_BYTES.match(line)
        if m:
            self.statistics.bytes_total = self._parse_size(m.group(1))
            self.statistics.bytes_copied = self._parse_size(m.group(2))
            self.progress.bytes_total = self.statistics.bytes_total
            self.progress.bytes_copied = self.statistics.bytes_copied
            
        m = self.RE_SPEED.search(line)
        if m:
            try:
                speed = float(m.group(1).replace(',', ''))
                self.progress.speed_mbps = speed / (1024 * 1024)
            except ValueError:
                pass
                
        self._update_percent()
        
    def _parse_size(self, s: str) -> int:
        """Parse size with suffix (k/m/g/t)"""
        s = s.strip().lower()
        mult = {'k': 1024, 'm': 1024**2, 'g': 1024**3, 't': 1024**4}
        for suf, m in mult.items():
            if suf in s:
                try:
                    return int(float(re.sub(r'[^\d\.]', '', s)) * m)
                except ValueError:
                    return 0
        try:
            return int(float(s.replace(',', '')))
        except ValueError:
            return 0
            
    def _update_percent(self):
        """Update overall percentage"""
        total = self._total_bytes or self.progress.bytes_total
        if total > 0 and self.progress.bytes_copied > 0:
            self.progress.percent = min((self.progress.bytes_copied / total) * 100, 100)
        elif self._total_files > 0:
            done = self._files_done + (self._cur_file_pct / 100 if self._cur_file_size else 0)
            self.progress.percent = min((done / self._total_files) * 100, 100)
            
    def get_progress(self) -> ProgressInfo:
        self._update_percent()
        return self.progress
        
    def get_statistics(self) -> CopyStatistics:
        return self.statistics
        
    def reset(self):
        """Reset for new operation"""
        totals = (self._total_bytes, self._total_files)
        self._reset_state()
        self._total_bytes, self._total_files = totals
