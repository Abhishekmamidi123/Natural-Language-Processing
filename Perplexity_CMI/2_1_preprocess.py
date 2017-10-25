# Read json file.
# Traverse the dictionary and Extract content from 'lang_tagged_text' and 'text' attributes.
# Split the content of the attributes (say a and b lists).
# If the first character of the word is "@", then remove this word form the list b and remove @ and its next element from list a. 
# Store the refined text in two different files(lang_tagged_text.txt: for finding CMI and text.txt: for finding Perplexity)

import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')

f1 = open('3_text.txt', 'w')
f2 = open('3_lang_tagged_text.txt', 'w')
# Data from json file
dataDict = {}

def readJsonFile(filename):
	with open(filename) as f:
		global dataDict
		dataDict = json.load(f)

def extractFromAttributes():
	for dic in dataDict:
		t = dic['text'].encode('ascii','ignore').split()
		ltt = dic['lang_tagged_text'].encode('ascii','ignore').split()
		t_final = []
		ltt_final = []
		
		for word in t:
			if word[0] != '@':
				t_final.append(word)
		
		cnt=0
		while(cnt<len(ltt)):
			if ltt[cnt][0]=='@':
				cnt+=2
			else:
				ltt_final.append(ltt[cnt][-2:])
				cnt+=1
			
		print ' '.join(t_final)
		print ' '.join(ltt_final)
		f1.write(' '.join(t_final))
		f1.write("\n")
		f2.write(' '.join(ltt_final))
		f2.write("\n")
	
# Read filename
filename=sys.argv[1]
# Read json object
readJsonFile(filename)
# Extract and write data
extractFromAttributes()
