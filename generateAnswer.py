# -*- coding: UTF-8 -*-
from gensim import models
import numpy as np

#載入維基詞向量模型，400維度
wiki_model = models.word2vec.Word2Vec.load("wiki_w2v.model")

#輸出最相近的前十個詞
def word2vec_predict(wiki_model,predictWord,top_k=10,verbose=False):
	try:
		predict = wiki_model.wv.similar_by_word(predictWord, topn=top_k)
		if verbose == True:
			for word in predict:
				print(word)
		else:
			for word in predict:
				print(word[0])
				#print(wiki_model[word[0]])
	except:
		print('字典裡沒這個詞!')


def generate_answer(wiki_model,predictWord,posibleAnswers):
	try:
		predict = wiki_model.wv.similar_by_word(predictWord, topn=10)
		for word in predict:
			if word[1]>0.5:
				posibleAnswers.append(word[0])
	except:
		return	



#產生相似的答案
posibleAnswers = []
top_k=10
verbose=False
index = 0
posibleAnswers.append("好")
while True:
	if len(posibleAnswers)>250 or index>len(posibleAnswers)-1:
		break
	else:
		generate_answer(wiki_model,posibleAnswers[index],posibleAnswers)
	index += 1

posibleAnswers = list(set(posibleAnswers))
posibleAnswers.sort()
posibleAnswers = np.array(posibleAnswers)
print(posibleAnswers)

with open('AnswerWords.txt', 'w') as filehandle:  
    for word in posibleAnswers:
        filehandle.write('%s\n' % word)

