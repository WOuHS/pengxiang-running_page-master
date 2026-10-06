import os
from config import GPX_FOLDER

print("GPX_FOLDER =", GPX_FOLDER)
all_files = os.listdir(GPX_FOLDER)
gpx_list = [f for f in all_files if f.lower().endswith(".gpx")]
print(f"原生os.listdir找到gpx数量：{len(gpx_list)}")
for name in gpx_list:
    print(" -", name)
