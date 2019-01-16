# -*- coding: UTF-8 -*-
import pysrt

#讀取字幕檔，將所有句子存入list
subtitles = []
subs = pysrt.open('ReadyPlayerOne.srt')
for lines in subs:
	line = lines.text.split()
	line[0] = line[0].replace('-','')
	subtitles.append(line[0])
	if len(line)==2:
		line[1] = line[1].replace('-','')
		subtitles.append(line[1])
#print(subtitles[0])


#讀取word2vec產生的文字檔，裡面有各種可能出現在回答中的詞
posibleAnswers = []
with open('AnswerWords.txt', 'r') as f:
	for line in f:
		line = line.replace('\n','')
		posibleAnswers.append(line)
#print(posibleAnswers[27])



question = []
answer = []
for num in range(len(posibleAnswers)):
	for index in range(len(subtitles)):
		if posibleAnswers[num] in subtitles[index]:
			question.append(subtitles[index-1])
			answer.append(subtitles[index])
			print(subtitles[index-1])
			print(subtitles[index])
			print('----')

