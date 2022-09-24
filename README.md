# addchapterstovideo-ffmpeg

**Easily add chapters to a video file with ffmpeg.**

## Usage

- get original metadata from video in **./ffmetadata.txt** file :
    - ``` ffmpeg -i INPUT -f ffmetadata FFMETADATAFILE ```
    - ``` ./ffmpeg -i '.\Phil Collins - Finally...The First Farewell Tour Paris 2004 HQ.480.mp4' -f ffmetadata ffmetadatafile.txt```
 
- parse a timestamp file (like **./chapters.txt**) with the python3 **./helper.py** script :
    - ``` python3 helper.py ``` - modify the parser or filenames in the script if needed
    
- append the content of the generated file **./FFMETADATAFILE** into **ffmetadata.txt**

- write the metadata file to the video :
    - ``` ffmpeg -i INPUT -i FFMETADATAFILE -map_metadata 1 -map_chapters 1 -codec copy OUTPUT ```
    - ``` ./ffmpeg -i '.\Phil Collins - Finally...The First Farewell Tour Paris 2004 HQ.480.mp4' -i ffmetadatafile.txt -map_metadata 1 -map_chapters 1 -codec copy output.mp4```

## See also

- https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg
- https://ffmpeg.org/ffmpeg-formats.html#Metadata-1
