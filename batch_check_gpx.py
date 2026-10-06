import os
import gpxpy

GPX_FOLDER = r"D:\0\Projects\runningpage2026code\GPX_OUT"
gpx_files = [f for f in os.listdir(GPX_FOLDER) if f.lower().endswith(".gpx")]

for fname in gpx_files:
    full_path = os.path.join(GPX_FOLDER, fname)
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            gpx = gpxpy.parse(f)
        track_count = len(gpx.tracks)
        route_count = len(gpx.routes)
        print(f"【{fname}】track:{track_count}, route:{route_count}")
        if track_count > 0:
            for t in gpx.tracks:
                for seg in t.segments:
                    if len(seg.points) > 0:
                        first_pt = seg.points[0]
                        has_time = first_pt.time is not None
                        print(f"  -> 首点是否带时间: {has_time}")
    except Exception as e:
        print(f"【{fname}】解析异常: {str(e)}")
