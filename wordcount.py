# put your code here.
# Find each unique word
import string
import sys
# make an empty dict
wordcount = {}
# open the file
file_data = open(sys.argv[1])
# iterate through the lines
for line in file_data:
# take off the new line 
	strip = line.rstrip()
# split by space
	words = strip.split(" ")
	for item in words:
# for each item in wordcount, add one!
#		for item in wordcount:
		lower_item = item.lower()
		lower_item = lower_item.translate(None, string.punctuation)
		value = wordcount.get(lower_item, 0) + 1
		wordcount[lower_item] = value
for k, v in wordcount.iteritems():
	print k, v


