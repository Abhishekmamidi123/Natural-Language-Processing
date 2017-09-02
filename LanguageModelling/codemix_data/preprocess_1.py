# encoding=utf8
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import preprocessor as p
f = open("train_1.txt", "w")
with open('train_data.json') as data_file:
	data = json.load(data_file)
print data
print "\n"
for item in data:
	print item["text"]
	l = item["text"].encode('ascii','ignore')
	f.write(l)
	f.write("\n")
	print item["text"]
	print "\n"
