import gpxpy
from datetime import datetime
import math

def get_distance(p1, p2):
    # running_page 使用的球面距离公式
    lon1, lat1 = math.radians(p1.longitude), math.radians(p1.latitude)
    lon2, lat2 = math.radians(p2.longitude), math.radians(p2.latitude)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371000 * c

fname = r"GPX_OUT\135780707.gpx"
with open(fname, "r", encoding="utf-8") as f:
    gpx = gpxpy.parse(f)

for track in gpx.tracks:
    for seg in track.segments:
        points = seg.points
        if len(points) < 2:
            print("点太少，跳过")
            continue
        start_time = points[0].time
        end_time = points[-1].time
        total_dist = 0
        for i in range(1, len(points)):
            total_dist += get_distance(points[i-1], points[i])
        duration = (end_time - start_time).total_seconds()
        print(f"文件: {fname}")
        print(f"起点时间: {start_time}")
        print(f"终点时间: {end_time}")
        print(f"总距离(m): {total_dist:.2f}")
        print(f"时长(s): {duration:.2f}")
        print("-"*40)
