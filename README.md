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

### Excetuion
Run the python file with the **-f** argument for the fast version. Otherwise the slower version will be executed.
```sh
python convert_videos.py (-f)
```