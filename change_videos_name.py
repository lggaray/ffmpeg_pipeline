import os
from shutil import move

path1 = 'RAWvideos/'
path2 = 'NAMvideos/'
path3 = 'RESvideos/'

files = os.listdir(path1)
for file in files:
    file_name = file.split('、')[0]
    inner_files = os.listdir(path1+file)
    right_video = [x for x in inner_files if '动画（右髋）' in x]
    left_video = [x for x in inner_files if '动画（左髋）' in x]
    try:
        move(path1+file+'/'+right_video[0], path2+file_name+'_right.mov')
    except:
        print('no right video')
    try:
        move(path1+file+'/'+left_video[0], path2+file_name+'_left.mov')
    except:
        print('no left video')
     
files = os.listdir(path2)
for file in files:
    file_name = file.split('.')[0]
    os.system('ffmpeg -i {} -preset fast -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 750k -minrate 400k -maxrate 1000k -bufsize 1500k -vf scale=-1:360 {}.mp4'.format(path2+file, path3+file_name))