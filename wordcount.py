# put your code here.
# Find each unique word
#intialize empty list
word_count_list = []
# make an empty dict
wordcount = {}
# open the file
file_data = open("test.txt")
# take off the new line 
# iterate through the lines
for line in file_data:
	strip = line.rstrip()
# split by space
	words = strip.split(" ")
# turn it all into list
	for item in words:
# for each item in wordcount, add one!
#		for item in wordcount:
		value = wordcount.get(item, 0) + 1
		wordcount[item] = value
for k, v in wordcount.iteritems():
	print k, v


# setify the list
#unique_words = set(word_count_list)

# keys in our dictionary first set dummy value
#for item in unique_words:
#	wordcount[item] = 0
# somewhere counting happens
# we have a list with all of the words
# dictionary with unique
#for item in word_count_list:
#	value = value + 1

# keys are from the unique set return which is now our dict
# values will come from the list since it has the repeat values
#for key, value in wordcount.iteritems():
#	value 
#	print key, value
#	value = 
#	wordcount[key] = #whatever number
# values number of times 
