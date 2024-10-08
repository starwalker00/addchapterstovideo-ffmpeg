import re

chapters = list()

with open('chapters.txt', 'r', encoding="utf8") as f:
   for line in f:
      print(line)
      x = re.match(r"(\d{2}):(\d{2}):(\d{2}) (.*)", line)
      print(x)
      hrs = int(x.group(1))
      mins = int(x.group(2))
      secs = int(x.group(3))
      title = x.group(4)

      minutes = (hrs * 60) + mins
      seconds = secs + (minutes * 60)
      timestamp = (seconds * 1000)
      chap = {
         "title": title,
         "startTime": timestamp
      }
      chapters.append(chap)

text = ""

for i in range(len(chapters)-1):
   chap = chapters[i]
   title = chap['title']
   start = chap['startTime']
   end = chapters[i+1]['startTime']-1
   text += f"""
[CHAPTER]
TIMEBASE=1/1000
START={start}
END={end}
title={title}
"""


with open("FFMETADATAFILE", "a") as myfile:
    myfile.write(text)
