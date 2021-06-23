#!/bin/bash

helpFunction()
{
   echo ""
   echo "Usage: $0 -a parameterA -b parameterB -c parameterC"
   echo -e "\t-a RAW videos path"
   echo -e "\t-b Converted videos path"
   exit 1 # Exit script after printing help
}

while getopts "a:b:c:" opt
do
   case "$opt" in
      a ) parameterA="$OPTARG" ;;
      b ) parameterB="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

# Print helpFunction in case parameters are empty
if [ -z "$parameterA" ] || [ -z "$parameterB" ]
then
   echo "Some or all of the parameters are empty";
   helpFunction
fi

# Begin script in case all parameters are correct

#generate .ini
#cd $parameterA
for file in $parameterA/*.IMA; do
  echo "Element: $file"
  ffmpeg -i $file -preset fast -codec:a libfdk_aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 750k -minrate 400k -maxrate 1000k -bufsize 1500k -vf scale=-1:360 $parameterB/output.mp4
  cmd
done
