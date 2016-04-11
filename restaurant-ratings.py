# your code goes here
import sys # open the file 

#define a list
rest_list = []
file_name = sys.argv[1]
file_data = open(file_name) # iterate and split data

for line in file_data: #take the newlines off

	strip = line.rstrip()
	rest_rating = strip.split(":")
	rest_list.append(rest_rating)

rest_list.sort()
	
for item in rest_list:
	rest, rating = item
	#append to list
	print "%s is rated at %s." % (rest, rating)
