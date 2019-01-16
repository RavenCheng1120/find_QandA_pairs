# -*- coding: UTF-8 -*-
import pysrt

#讀取字幕檔，將所有句子存入list
subtitles = []
subs = pysrt.open('ReadyPlayerOne.srt')
for lines in subs:
	line = lines.text.split()
	subtitles.append(line[0])
	if len(line)==2:
		subtitles.append(line[1])
#print(subtitles[0])

#讀取文字檔案
posibleAnswers = []
with open('AnswerWords.txt', 'r') as f:
	for line in f:
		line = line.replace('\n','')
		posibleAnswers.append(line)
print(posibleAnswers)

question = []
answer = []
