# !/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
import preprocessor as p
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer
porter = PorterStemmer()
f = open("data/abhi.txt","w")
with open("/home/abhishek/Desktop/SEM_5/H/LanguageModelling/data/test") as file:
	cnt=1
	for line in file:
		
		print cnt
		cnt+=1
		words=line.split()
		l=[]
		for i in range(1,len(words)-3):
			if words[i][0]!='@':
				l.append(words[i])
		f.write(" ".join(l)+"\n")
f.close()
