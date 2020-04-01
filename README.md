# OpenH264 FFmpeg py

## Usage

```shell
$ docker build -t openh264-ffmpeg-py .
$ docker run --rm -it openh264-ffmpeg-py
ffmpeg version n4.2.2 Copyright (c) 2000-2019 the FFmpeg developers
built with gcc 8 (Debian 8.3.0-6)
configuration: --enable-libopenh264 --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libvpx
libavutil      56. 31.100 / 56. 31.100
libavcodec     58. 54.100 / 58. 54.100
libavformat    58. 29.100 / 58. 29.100
libavdevice    58.  8.100 / 58.  8.100
libavfilter     7. 57.100 /  7. 57.100
libswscale      5.  5.100 /  5.  5.100
libswresample   3.  5.100 /  3.  5.100
```

## Notes

`install_ffmpeg_supporting_openh264.sh` is originally copied from [contribu/install_ffmpeg_supporting_openh264.sh |  Github Gist](https://gist.github.com/contribu/8a572edaccb86ae749449a3fec83ce5f) and modified versions of openh264 & ffmpeg.
