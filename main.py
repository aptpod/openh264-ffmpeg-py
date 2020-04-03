from pprint import pprint

import ffmpeg

if __name__ == '__main__':
    print('original file info:', flush=True)
    info = ffmpeg.probe('/movies/original.mov')
    pprint(info)
    
    fps = eval(info['streams'][0]['avg_frame_rate'])

    print('\ndecode it to jpeg images:', flush=True)
    ffmpeg.input('/movies/original.mov').output('/tmp/%05d.jpg', r=fps).run()
    print('\n------\n', flush=True)
    print('\nre-encode them to a mp4 file using libopenh264:', flush=True)
    ffmpeg.input('/tmp/%05d.jpg', r=fps).output('/movies/re-encoded.mp4', r=fps, vcodec='libopenh264').run()

    print('\nre-encoded file info:', flush=True)
    info = ffmpeg.probe('/movies/re-encoded.mp4')
    pprint(info)