import platform
import shutil
import os
from datetime import datetime
disk = shutil.disk_usage("/")
used_percent=disk.used/disk.total*100
print("SYSTEM SCOUT")
print("="*50)
print("Scan time:", datetime.now())
print("Operating system:", platform.system(), platform.release())
print("Processor:", platform.processor() or platform.machine())
print("Logical CPUs:", os.cpu_count())
print("-" * 50)
print("Total disk:", round(disk.total / (1024 ** 3), 1), "GiB")
print("Free disk:", round(disk.free / (1024 ** 3), 1), "GiB")
print("Disk usage:", round(used_percent, 1), "%")
filled = round(used_percent / 4)
print("[" + "#" * filled + "-" * (25 - filled) + "]")
print("Scan complete.")

# Check storage usage.
if used_percent >= 80:
    status = "WARNING: Disk usage is at or above 80%."
else:
    status = "OK: Disk usage is below 80%."

print()
print("Storage status:", status)

# Build a readable system report.
report = f"""SYSTEM SCOUT REPORT
==================================================
Scan time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Operating system: {platform.system()} {platform.release()}
Processor: {platform.processor() or platform.machine()}
Logical CPUs: {os.cpu_count()}

STORAGE — ROOT FILESYSTEM
--------------------------------------------------
Total disk: {disk.total / (1024 ** 3):.1f} GiB
Used disk: {disk.used / (1024 ** 3):.1f} GiB
Free disk: {disk.free / (1024 ** 3):.1f} GiB
Disk usage: {used_percent:.1f}%

Storage status: {status}
==================================================
"""

# Use a timestamp to distinguish reports from different scans.
report_name = datetime.now().strftime("system_report_%Y%m%d_%H%M%S.txt")

# Save the report and handle any file-writing error.
try:
    with open(report_name, "w", encoding="utf-8") as report_file:
        report_file.write(report)
    print("Report saved:", report_name)
except OSError as error:
    print("Could not save the report:", error)
