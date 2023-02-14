import json
import yt_dlp

URL = "https://youtu.be/e6YdVth4G-U"

# ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(URL, download=False)

   
json_object = json.dumps(info, indent=4)
# Writing to sample.json

with open("Neptune.json", "w") as outfile:

    outfile.write(json_object)