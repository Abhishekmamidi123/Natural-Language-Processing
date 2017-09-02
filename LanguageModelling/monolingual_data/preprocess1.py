# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import preprocessor as p
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer
porter = PorterStemmer()
f = open("data/vag.txt","w")
with open("/home/abhishek/Desktop/SEM_5/H/LanguageModelling/data/conversations1.txt") as file:
	cnt=1
	for line in file:
		print cnt
		cnt+=1
		line=p.clean(line)
		# split to words: We've --> We have
		line=line.lower()
		wordList=wordpunct_tokenize(line)
		if len(wordList)!=0:
			line=""
			for i in wordList:
				i=porter.stem(i)
				if re.findall(r'\W',i)==[]:
					line=line+i+" "
			if line.strip()!='':
				f.write(line+"\n")
f.close()
