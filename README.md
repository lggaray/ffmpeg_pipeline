# Video Conversion Pipeline
## _(using ffmpeg)_

There's a _fast_ version which consist in just change the video file extension to _mov_.
The problem with this version is that sometimes the video encoding has problems.

There's also a _slow_ version which uses the **ffmpeg**. It's slower, but ensures there's no encoding problem.

## Directories

There are three main directories:

- RAWvideos: where the input raw videos are located
- NAMEvideos: where the changed name/extension videos are located
- RESvideos: where the final output is located

### Video Quality
MP4 - 1080p
```sh
ffmpeg -i input.mov -preset slow -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 4500k -minrate 4500k -maxrate 9000k -bufsize 9000k -vf scale=-1:1080 output.mp4
```

MP4 - 720p
```sh
ffmpeg -i input.mov -preset slow -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 2500k -minrate 1500k -maxrate 4000k -bufsize 5000k -vf scale=-1:720 output.mp4
```

MP4 - 480p
```sh
ffmpeg -i input.mov -preset slow -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 1000k -minrate 500k -maxrate 2000k -bufsize 2000k -vf scale=854:480 output.mp4
```

MP4 - 360p
```sh
ffmpeg -i input.mov -preset slow -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 750k -minrate 400k -maxrate 1000k -bufsize 1500k -vf scale=-1:360 output.mp4
```

### Excetuion
Run the python file with the **-f** argument for the fast version. Otherwise the slower version will be executed.
```sh
python convert_videos.py (-f)
```