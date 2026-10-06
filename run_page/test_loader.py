from gpxtrackposter import track_loader
from config import GPX_FOLDER

loader = track_loader.TrackLoader()
tracks = loader.load_tracks(GPX_FOLDER, file_suffix="gpx")
print(f"track loader读取到track数量: {len(tracks)}")
for t in tracks:
    print(t.file_names)
