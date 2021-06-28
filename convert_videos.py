import os, argparse
from shutil import move

path1 = 'RAWvideos/' ### Input videos
path2 = 'NAMvideos/' ### Named videos (only change name and extension)
path3 = 'RESvideos/' ### Final output

'''
Fast conversion (only changing the file extension), 
but running video detection could face the
          << moov atom not found >>
problem.


Slow conversion (using ffmpeg) but it ensures running
video detection won't face the 
    << moov atom not found >>
problem.
'''

### check whether FAST MODE is activated or not
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fast", help="run the fast version", action="store_true")
args = parser.parse_args()

files = os.listdir(path1)
for file in files:
    file_name = file.split('、')[0]
    inner_files = os.listdir(path1+file)
    right_video = [x for x in inner_files if '动画（右髋）' in x]
    left_video = [x for x in inner_files if '动画（左髋）' in x]
    if args.fast:
        try:
            move(path1+file+'/'+right_video[0], path2+file_name+'_right.mov')
        except:
            print('no right video')
        try:
            move(path1+file+'/'+left_video[0], path2+file_name+'_left.mov')
        except:
            print('no left video')
    else:
        try:
            move(path1+file+'/'+right_video[0], path2+file_name+'_right.IMA')
        except:
            print('no right video')
        try:
            move(path1+file+'/'+left_video[0], path2+file_name+'_left.IMA')
        except:
            print('no left video')
     
        new_files = os.listdir(path2)
        for nfile in new_files:
            nfile_name = nfile.split('.')[0]
            os.system('ffmpeg -i {} -preset fast -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 750k -minrate 400k -maxrate 1000k -bufsize 1500k -vf scale=-1:360 {}.mp4'.format(path2+nfile, path3+nfile_name))
            os.remove(path2+nfile)

print('+++++++++++++++++++++++++++++++')
if args.fast:
    print('FAST VIDEO CONVERSION FINISHED')
else:
    print('SLOW VIDEO CONVERSION FINISHED')
print('+++++++++++++++++++++++++++++++')