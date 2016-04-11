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
		word_count_list.append(item)
# setify the list
print word_count_list
# keys in our dictionary first set dummy values


# somewhere counting happens
# values number of times 
