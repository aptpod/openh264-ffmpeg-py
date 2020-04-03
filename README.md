# OpenH264 FFmpeg py

## Usage

```shell
$ docker build -t openh264-ffmpeg-py .
$ docker run --rm --mount type=bind,src=$(pwd)/movies,dst=/movies openh264-ffmpeg-py
original file info:
{'format': {'bit_rate': '3428852',
            'duration': '6.016667',
            'filename': '/movies/original.mov',
            'format_long_name': 'QuickTime / MOV',
            'format_name': 'mov,mp4,m4a,3gp,3g2,mj2',
            'nb_programs': 0,
            'nb_streams': 1,
            'probe_score': 100,
            'size': '2578783',
            'start_time': '0.000000',
            'tags': {'com.apple.quicktime.creationdate': '2020-04-03T12:04:59+0900',
                     'com.apple.quicktime.make': 'Apple',
                     'com.apple.quicktime.model': 'MacBookPro14,2',
                     'com.apple.quicktime.software': 'Mac OS X 10.15.3 (19D76)',
                     'compatible_brands': 'qt  ',
                     'creation_time': '2020-04-03T03:04:59.000000Z',
                     'major_brand': 'qt  ',
                     'minor_version': '0'}},
 'streams': [{'avg_frame_rate': '60/1',
              'bit_rate': '3370753',
              'bits_per_raw_sample': '8',
              'chroma_location': 'left',
              'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10',
              'codec_name': 'h264',
              'codec_tag': '0x31637661',
              'codec_tag_string': 'avc1',
              'codec_time_base': '1/120',
              'codec_type': 'video',
              'coded_height': 736,
              'coded_width': 2064,
              'color_primaries': 'bt709',
              'color_range': 'tv',
              'color_space': 'bt709',
              'color_transfer': 'bt709',
              'display_aspect_ratio': '513:182',
              'disposition': {'attached_pic': 0,
                              'clean_effects': 0,
                              'comment': 0,
                              'default': 1,
                              'dub': 0,
                              'forced': 0,
                              'hearing_impaired': 0,
                              'karaoke': 0,
                              'lyrics': 0,
                              'original': 0,
                              'timed_thumbnails': 0,
                              'visual_impaired': 0},
              'duration': '6.016667',
              'duration_ts': 36100,
              'has_b_frames': 16,
              'height': 728,
              'index': 0,
              'is_avc': 'true',
              'level': 42,
              'nal_length_size': '4',
              'nb_frames': '363',
              'pix_fmt': 'yuv420p',
              'profile': 'Main',
              'r_frame_rate': '60/1',
              'refs': 1,
              'sample_aspect_ratio': '1:1',
              'start_pts': 0,
              'start_time': '0.000000',
              'tags': {'creation_time': '2020-04-03T03:04:59.000000Z',
                       'encoder': 'H.264',
                       'handler_name': 'Core Media Video',
                       'language': 'und'},
              'time_base': '1/6000',
              'width': 2052}]}

decode it to jpeg images
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
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from '/movies/original.mov':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    creation_time   : 2020-04-03T03:04:59.000000Z
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: MacBookPro14,2
    com.apple.quicktime.software: Mac OS X 10.15.3 (19D76)
    com.apple.quicktime.creationdate: 2020-04-03T12:04:59+0900
  Duration: 00:00:06.02, start: 0.000000, bitrate: 3428 kb/s
    Stream #0:0(und): Video: h264 (Main) (avc1 / 0x31637661), yuv420p(tv, bt709), 2052x728 [SAR 1:1 DAR 513:182], 3370 kb/s, 60 fps, 60 tbr, 6k tbn, 12k tbc (default)
    Metadata:
      creation_time   : 2020-04-03T03:04:59.000000Z
      handler_name    : Core Media Video
      encoder         : H.264
Stream mapping:
  Stream #0:0 -> #0:0 (h264 (native) -> mjpeg (native))
Press [q] to stop, [?] for help
[swscaler @ 0x55b5fa028580] deprecated pixel format used, make sure you did set range correctly
Output #0, image2, to '/tmp/%05d.jpg':
  Metadata:
    major_brand     : qt  
    minor_version   : 0
    compatible_brands: qt  
    com.apple.quicktime.creationdate: 2020-04-03T12:04:59+0900
    com.apple.quicktime.make: Apple
    com.apple.quicktime.model: MacBookPro14,2
    com.apple.quicktime.software: Mac OS X 10.15.3 (19D76)
    encoder         : Lavf58.29.100
    Stream #0:0(und): Video: mjpeg, yuvj420p(pc), 2052x728 [SAR 1:1 DAR 513:182], q=2-31, 200 kb/s, 60 fps, 60 tbn, 60 tbc (default)
    Metadata:
      creation_time   : 2020-04-03T03:04:59.000000Z
      handler_name    : Core Media Video
      encoder         : Lavc58.54.100 mjpeg
    Side data:
      cpb: bitrate max/min/avg: 0/0/200000 buffer size: 0 vbv_delay: -1
frame=  361 fps=124 q=24.8 Lsize=N/A time=00:00:06.01 bitrate=N/A speed=2.06x
video:9433kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown

------


re-encode them to a mp4 file using libopenh264:
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
Input #0, image2, from '/tmp/%05d.jpg':
  Duration: 00:00:14.44, start: 0.000000, bitrate: N/A
    Stream #0:0: Video: mjpeg (Baseline), yuvj420p(pc, bt470bg/unknown/unknown), 2052x728 [SAR 1:1 DAR 513:182], 25 fps, 25 tbr, 25 tbn, 25 tbc
Stream mapping:
  Stream #0:0 -> #0:0 (mjpeg (native) -> h264 (libopenh264))
Press [q] to stop, [?] for help
[swscaler @ 0x557701db5b40] deprecated pixel format used, make sure you did set range correctly
[libopenh264 @ 0x557701a6f400] [OpenH264] this = 0x0x557701a750d0, Warning:bEnableFrameSkip = 0,bitrate can't be controlled for RC_QUALITY_MODE,RC_BITRATE_MODE and RC_TIMESTAMP_MODE without enabling skip frame.
[libopenh264 @ 0x557701a6f400] [OpenH264] this = 0x0x557701a750d0, Warning:Change QP Range from(0,51) to (12,42)
Output #0, mp4, to '/movies/re-encoded.mp4':
  Metadata:
    encoder         : Lavf58.29.100
    Stream #0:0: Video: h264 (libopenh264) (avc1 / 0x31637661), yuv420p, 2052x728 [SAR 1:1 DAR 513:182], q=2-31, 200 kb/s, 60 fps, 15360 tbn, 60 tbc
    Metadata:
      encoder         : Lavc58.54.100 libopenh264
    Side data:
      cpb: bitrate max/min/avg: 200000/0/200000 buffer size: 0 vbv_delay: -1
frame=  362 fps=103 q=-0.0 Lsize=    1002kB time=00:00:06.01 bitrate=1363.8kbits/s dup=1 drop=0 speed=1.71x
video:999kB audio:0kB subtitle:0kB other streams:0kB global headers:0kB muxing overhead: 0.233953%

re-encoded file info:
{'format': {'bit_rate': '1359863',
            'duration': '6.034000',
            'filename': '/movies/re-encoded.mp4',
            'format_long_name': 'QuickTime / MOV',
            'format_name': 'mov,mp4,m4a,3gp,3g2,mj2',
            'nb_programs': 0,
            'nb_streams': 1,
            'probe_score': 100,
            'size': '1025677',
            'start_time': '0.000000',
            'tags': {'compatible_brands': 'isomiso2avc1mp41',
                     'encoder': 'Lavf58.29.100',
                     'major_brand': 'isom',
                     'minor_version': '512'}},
 'streams': [{'avg_frame_rate': '60/1',
              'bit_rate': '1356839',
              'bits_per_raw_sample': '8',
              'chroma_location': 'left',
              'codec_long_name': 'H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10',
              'codec_name': 'h264',
              'codec_tag': '0x31637661',
              'codec_tag_string': 'avc1',
              'codec_time_base': '1/120',
              'codec_type': 'video',
              'coded_height': 736,
              'coded_width': 2064,
              'display_aspect_ratio': '513:182',
              'disposition': {'attached_pic': 0,
                              'clean_effects': 0,
                              'comment': 0,
                              'default': 1,
                              'dub': 0,
                              'forced': 0,
                              'hearing_impaired': 0,
                              'karaoke': 0,
                              'lyrics': 0,
                              'original': 0,
                              'timed_thumbnails': 0,
                              'visual_impaired': 0},
              'duration': '6.033333',
              'duration_ts': 92672,
              'has_b_frames': 0,
              'height': 728,
              'index': 0,
              'is_avc': 'true',
              'level': 42,
              'nal_length_size': '4',
              'nb_frames': '362',
              'pix_fmt': 'yuv420p',
              'profile': 'Constrained Baseline',
              'r_frame_rate': '60/1',
              'refs': 1,
              'sample_aspect_ratio': '1:1',
              'start_pts': 0,
              'start_time': '0.000000',
              'tags': {'handler_name': 'VideoHandler', 'language': 'und'},
              'time_base': '1/15360',
              'width': 2052}]}
```

## Notes

`install_ffmpeg_supporting_openh264.sh` is originally copied from [contribu/install_ffmpeg_supporting_openh264.sh |  Github Gist](https://gist.github.com/contribu/8a572edaccb86ae749449a3fec83ce5f) and modified versions of openh264 & ffmpeg.
