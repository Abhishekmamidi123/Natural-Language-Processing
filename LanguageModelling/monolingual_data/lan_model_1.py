# Goal:
# Apply different language models like unigram, bigram, trigram on the given twitter corpus and codemixed corpus.
# Find CMI and Perplexity for each of the above models.
# Compare perplexity and analyse the best among them.

# Steps:
# Preprocess the data (Apply tokenization and stemming).
# Store all the words(V) in a dictionary with unique id's and their frequencies in a list.
# Create a V*V matrix with all bigram totalLiness.
# Apply add-one smoothing on the matrix.
# For every sentence in the corpus, find probabilities P( word(n)|word(n-1) ) of each word in the sequence and thereby find the perplexity of each sentence.
# Take the average of all the perplexities.
# Analyse the perplexities of different models.

# Variables:
# wordDict: Dictionary which stores all the words.
# index: To give unique id's to every word in the dictionary.
# V: Vocabulary size.

# Code
import numpy as np
import nltk
import os
import sys
# from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
import json
import re
# porter = PorterStemmer()

# Put words in dictionary
index=0		# Index of word in dictionary
totalLines=0		# Total number of lines
tokens=0	# Total number of words in the corpus
V=0
V_tri=0
matrix={}
triMatrix = {}
wordDict = {}
bigram_perplex=[]
secondDict={}

def get_count():
	global index
	return index

def createBiMatrix():
	global matrix
	matrix = {}

def createTriMatrix():
	global triMatrix
	triMatrix = {}

def putInDict(filename):
	global totalLines, tokens, index
	with open(filename) as file:
		for line in file:
			totalLines+=1
			# line = "My name is Abhishek and the name of the boy who was standing there is not Abhishek"
			listOfWords = wordpunct_tokenize(line)
			tokens = tokens + len(listOfWords)
			for word in listOfWords:
				# word = porter.stem(word)
				if word in wordDict:
					wordDict[word][1]+=1
				else:
					wordDict[word] = [index, 1]
					index+=1
	# print wordDict

def unigramPerplexity():
	global filename, totalLines, tokens, index
	with open(filename) as file:
		perplexities=[]
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			prob=[]
			for i in range(l):
				word=listOfWords[i]
				prob.append(wordDict[word][1]/float(tokens))
			per=1
			for p in prob:
        			per = per*p
        		if per!=0:
        			per=1/float(per)
        		perplexities.append(pow(per, 1/float(l)))
	PP=0
	for i in perplexities:
		PP=PP+i
	PP=PP/float(len(perplexities))
	return PP

def createBigram():
	global filename, totalLines, tokens, index
	with open(filename) as file:
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			if l!=0:
				word = listOfWords[0]
				key = str(["",word])
				if key not in matrix:
					matrix[key] = 1
				else:
					matrix[key] += 1	
				# matrix[V][wordDict[word][0]]+=1	
			for i in range(l-1):
				word = listOfWords[i]
				next_word = listOfWords[i+1]
				key = str([word,next_word])
				if key not in matrix:
					matrix[key] = 1
				else:
					matrix[key] += 1
				# matrix[wordDict[word][0]][wordDict[next_word][0]]+=1
	# print wordDict
	# print matrix
	
def bigramPerplexity():
	global filename, totalLines, tokens, index
	with open(filename) as file:
		perplexities=[]
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			prob=[]
			if l!=0:
				word=listOfWords[0]
				prob.append(matrix[str(["", word])]/float(totalLines))
				# prob.append(matrix[V][wordDict[word][0]]/float(totalLines))
			for i in range(l-1):
				word=listOfWords[i]
				next_word = listOfWords[i+1]
				prob.append(matrix[str([word, next_word])]/float(wordDict[word][1]))
				# prob.append(matrix[wordDict[word][0]][wordDict[next_word][0]]/float(wordDict[word][1]))
			# Find perplexity
			# print prob
			per=1
			for p in prob:
        			per = per*p
        		if per!=0:
        			per=1/float(per)
        		perplexities.append(pow(per, 1/float(l)))
	# print perplexities
	PP=0
	for i in perplexities:
		PP=PP+i
	PP=PP/float(len(perplexities))
	return PP

def trigramDict():
	global filename, totalLines, tokens, index
	index=0
	with open(filename) as file:
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			if l!=0:
				word=listOfWords[0]
				if word in secondDict:
					secondDict[str(word)]+=1
				else:
					secondDict[str(word)]=1
				if l>1:
					word1=listOfWords[1]
					s=str([word,word1])
					if s in secondDict:
						 secondDict[s]+=1
					else:
						secondDict[s]=1
			# for i in range(l-1):
			#	s = str([listOfWords[i],listOfWords[i+1]])
			#	if s in trigram_dict:
			#		trigram_dict[s][1]+=1
			#	else:
			#		trigram_dict[s]=[index, 1]
			#		index+=1
	# print "\n"
	# print trigram_dict
	# print "\n"
	# print secondDict
	# print "\n"

def createTrigram():
	global filename, totalLines, tokens, index
	with open(filename) as file:
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			for i in range(l-2):
				word1 = listOfWords[i]
				word2 = listOfWords[i+1]
				word3 = listOfWords[i+2]
				key = str([word1,word2,word3])
				if key not in triMatrix:
					triMatrix[key] = 1
				else:
					triMatrix[key] += 1
				# matrix[trigram_dict[s][0]][wordDict[word3][0]]+=1
	# print triMatrix

def trigramPerplexity():
	global filename, totalLines, tokens, index
	with open(filename) as file:
		perplexities=[]
		for line in file:
			listOfWords = wordpunct_tokenize(line)
			l = len(listOfWords)
			prob=[]
			if l!=0:
				word=listOfWords[0]
				prob.append(secondDict[str(word)]/float(totalLines))		
				if l>1:
					word1=listOfWords[1]
					prob.append(secondDict[str([word,word1])]/float(totalLines))
			for i in range(l-2):
				word1 = listOfWords[i]
				word2 = listOfWords[i+1]
				word3 = listOfWords[i+2]
				s = str([word1,word2])
				num = triMatrix[str([word1,word2,word3])]
				# num = matrix[trigram_dict[s][0]][wordDict[word][0]]
				den = matrix[s]
				prob.append(float(num)/float(den))
			per=1
			# print prob
			for p in prob:
        			per = per*p
        		if per!=0:
        			per=1/float(per)
        		perplexities.append(pow(per, 1/float(l)))
	PP=0
	# print perplexities
	for i in perplexities:
		PP=PP+i
	PP=PP/float(len(perplexities))
	return PP
				
#########################################################################################

# Main
filename=sys.argv[1]
putInDict(filename)
V=get_count()
# Unigram
unigramPP = unigramPerplexity()
print "Unigram Perplexity = "+str(unigramPP)
# Bigram
createBiMatrix()
createBigram()
bigramPP = bigramPerplexity()
print "Bigram Perplexity = "+str(bigramPP)
print "==========================================================="
# Trigram
index=0
trigramDict()
V_tri=get_count()
createTriMatrix()
createTrigram()
trigramPP = trigramPerplexity()
print "Trigram Perplexity = "+str(trigramPP)
print "Found perplexity"
print "Done."

# Just for printing
#for word in wordDict:
#	print word, wordDict[word]
