import os
from shutil import move

path1 = 'RAWvideos/'
path2 = 'RESvideos/'
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
       