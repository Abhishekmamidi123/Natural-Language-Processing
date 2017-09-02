# !/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import preprocessor as p
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer
porter = PorterStemmer()
f = open("train_2.txt","w")
with open("/home/nlp/Desktop/LanguageModelling/codemix_data/train_1.txt") as file:
	cnt=1
	for line in file:
		print cnt
		cnt+=1
		words=line.split()
		l=[]
		for i in range(len(words)):
			if words[i][0]!='@':
				l.append(words[i])
		f.write(" ".join(l)+"\n")
f.close()
