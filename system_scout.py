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

