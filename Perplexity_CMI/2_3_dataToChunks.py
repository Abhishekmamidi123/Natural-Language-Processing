# Divide data into chunks and store in seperate files based on the range of perplexities in the order of 10 from 0 to 100.
# "3_CMI_values.txt" contains CMI values for about 11000 tweets.

# Initialization
CMI_values = []

# Read CMI values and store them in the list.
def getCMIValues(filename):
	f =open(filename, 'r')
	global CMI_values
	CMI_values = f.readlines()

# Divide the data into Chunks and store in seperate files.
def divideDataIntoChunks():
	f1 = open("Chunks/0_10.txt", 'w')
	f2 = open("Chunks/10_20.txt", 'w')
	f3 = open("Chunks/20_30.txt", 'w')
	f4 = open("Chunks/30_40.txt", 'w')
	f5 = open("Chunks/40_50.txt", 'w')
	f6 = open("Chunks/50_60.txt", 'w')
	f7 = open("Chunks/60_70.txt", 'w')
	f8 = open("Chunks/70_80.txt", 'w')
	f9 = open("Chunks/80_90.txt", 'w')
	f10 = open("Chunks/90_100.txt", 'w')
	f = open("3_text.txt", 'r')
	cnt=0
	for line in f:
		print cnt
		print CMI_values[cnt][:-1]
		cmi = float(CMI_values[cnt][:-1])
		if cmi>=0 and cmi<=10:
			f1.write(line)
		elif cmi>10 and cmi<=20:
			f2.write(line)
		elif cmi>20 and cmi<=30:
			f3.write(line)
		elif cmi>30 and cmi<=40:
			f4.write(line)
		elif cmi>40 and cmi<=50:
			f5.write(line)
		elif cmi>50 and cmi<=60:
			f6.write(line)
		elif cmi>60 and cmi<=70:
			f7.write(line)
		elif cmi>70 and cmi<=80:
			f8.write(line)
		elif cmi>80 and cmi<=90:
			f9.write(line)
		elif cmi>90 and cmi<=100:
			f10.write(line)
		cnt+=1

filename = "3_CMI_values.txt"
# filename = "x.txt"
getCMIValues(filename)
divideDataIntoChunks()
