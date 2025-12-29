"""
FastCopy - Utilities v1.4
Helper functions for file operations and disk info.
"""
import os
import ctypes
import shutil
import subprocess
from typing import Tuple, Optional
from dataclasses import dataclass


def format_size(b: int, precision: int = 2) -> str:
    """Format bytes to human readable"""
    if b <= 0:
        return "0 B"
    for u in ['B', 'KB', 'MB', 'GB', 'TB']:
        if b < 1024:
            return f"{int(b)} {u}" if u == 'B' else f"{b:.{precision}f} {u}"
        b /= 1024
    return f"{b:.{precision}f} PB"


def format_time(s: float) -> str:
    """Format seconds to readable time"""
    s = max(0, int(s))
    if s < 60:
        return f"{s}s"
    if s < 3600:
        return f"{s // 60}m {s % 60}s"
    return f"{s // 3600}h {(s % 3600) // 60}m"


def get_folder_size(path: str) -> Tuple[int, int]:
    """Get folder total size and file count"""
    total, count = 0, 0
    try:
        for root, _, files in os.walk(path):
            for f in files:
                try:
                    total += os.path.getsize(os.path.join(root, f))
                    count += 1
                except OSError:
                    pass
    except OSError:
        pass
    return total, count


@dataclass
class DiskInfo:
    """Disk drive information"""
    drive_letter: str = ""
    label: str = ""
    file_system: str = ""
    drive_type: str = ""
    model: str = ""
    serial: str = ""
    total_bytes: int = 0
    used_bytes: int = 0
    free_bytes: int = 0
    
    @property
    def used_percent(self) -> float:
        return (self.used_bytes / self.total_bytes * 100) if self.total_bytes else 0
    
    @property
    def free_percent(self) -> float:
        return (self.free_bytes / self.total_bytes * 100) if self.total_bytes else 0


def get_disk_info(path: str) -> Optional[DiskInfo]:
    """Get disk info for path"""
    try:
        drive = os.path.splitdrive(os.path.abspath(path))[0]
        if not drive:
            return None
            
        letter = drive.rstrip(':')
        drive_path = drive + '\\'
        
        # Disk space
        try:
            total, used, free = shutil.disk_usage(drive_path)
        except OSError:
            total, used, free = 0, 0, 0
            
        # Volume info
        label, fs = "", ""
        try:
            vol_buf = ctypes.create_unicode_buffer(256)
            fs_buf = ctypes.create_unicode_buffer(256)
            ctypes.windll.kernel32.GetVolumeInformationW(
                drive_path, vol_buf, 256, None, None, None, fs_buf, 256
            )
            label = vol_buf.value or f"Drive {letter}"
            fs = fs_buf.value
        except OSError:
            label = f"Drive {letter}"
            
        # Drive type
        dtype = "Unknown"
        try:
            code = ctypes.windll.kernel32.GetDriveTypeW(drive_path)
            dtype = {2: "USB", 3: "HDD/SSD", 4: "Network", 5: "CD-ROM"}.get(code, "Unknown")
        except OSError:
            pass
            
        # Get model via PowerShell
        model, serial, media = "", "", ""
        try:
            ps = f"$p=Get-Partition -DriveLetter '{letter}' -EA 0;if($p){{$d=Get-PhysicalDisk|?{{$_.DeviceId -eq $p.DiskNumber}};\"$($d.Model)|$($d.SerialNumber)|$($d.MediaType)\"}}"
            r = subprocess.run(['powershell', '-Command', ps], capture_output=True, text=True, timeout=3, creationflags=0x08000000)
            if r.returncode == 0 and r.stdout.strip():
                parts = r.stdout.strip().split('|')
                if len(parts) >= 3:
                    model, serial, media = parts[0].strip(), parts[1].strip(), parts[2].strip()
                    if 'SSD' in media.upper():
                        dtype = 'SSD'
                    elif 'NVMe' in model.upper():
                        dtype = 'NVMe'
                    elif 'HDD' in media.upper():
                        dtype = 'HDD'
        except (subprocess.TimeoutExpired, OSError):
            pass
            
        return DiskInfo(letter, label, fs, dtype, model, serial, total, used, free)
        
    except Exception:
        return None


def check_disk_space_warning(src_size: int, dst_path: str) -> Tuple[bool, str]:
    """Check if destination has enough space"""
    if src_size <= 0:
        return False, ""
    info = get_disk_info(dst_path)
    if not info:
        return False, ""
    if src_size >= info.free_bytes:
        return True, f"Cần: {format_size(src_size)} | Còn: {format_size(info.free_bytes)}"
    remaining_pct = (info.free_bytes - src_size) / info.total_bytes * 100 if info.total_bytes else 0
    if remaining_pct < 10:
        return True, f"Sau copy còn {remaining_pct:.1f}% trống"
    return False, ""


def get_system_performance_info() -> Tuple[bool, str]:
    """Get system info (CPU, RAM)"""
    info = []
    try:
        # CPU
        r = subprocess.run(
            ['powershell', '-Command', '(Get-WmiObject Win32_Processor).Name'],
            capture_output=True, text=True, timeout=2, creationflags=0x08000000
        )
        if r.returncode == 0:
            info.append(f"CPU: {r.stdout.strip()}")
            
        # RAM
        r = subprocess.run(
            ['powershell', '-Command', '[math]::Round((Get-WmiObject Win32_ComputerSystem).TotalPhysicalMemory/1GB,1)'],
            capture_output=True, text=True, timeout=2, creationflags=0x08000000
        )
        if r.returncode == 0:
            info.append(f"RAM: {r.stdout.strip()} GB")
    except (subprocess.TimeoutExpired, OSError):
        pass
        
    return False, "✅ " + " | ".join(info) if info else "✅ Hệ thống OK"


def parse_buffer_size(value: str, unit: str) -> int:
    """Parse buffer size with unit"""
    try:
        num = float(value)
        mult = {'KB': 1024, 'MB': 1024**2, 'GB': 1024**3}
        return int(num * mult.get(unit, 1024**2))
    except ValueError:
        return 8 * 1024 * 1024
