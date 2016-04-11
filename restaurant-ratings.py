# your code goes here
import sys # open the file 


rest_list = [] #define a list
file_name = sys.argv[1]
file_data = open(file_name) # iterate and split data

for line in file_data: #take the newlines off

	strip = line.rstrip()
	rest_rating = strip.split(":")
	rest_list.append(rest_rating)

rest_list.sort()
	
for x in rest_list:
	rest, rating = x
	print "%s is rated at %s." % (rest, rating)
