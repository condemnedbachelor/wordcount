# your code goes here
import sys # open the file 

file_name = sys.argv[1]
file_data = open(file_name) # iterate and split data

for line in file_data: #take the newlines off

	strip = line.rstrip()
	rest_rating = strip.split(":")

	rest, rating = rest_rating
	print "%s is rated at %s." % (rest, rating)
