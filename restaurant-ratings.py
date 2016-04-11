# your code goes here
import sys # open the file 


rest_dict = {} #define a dict
file_name = sys.argv[1]
file_data = open(file_name) # iterate and split data

for line in file_data: #take the newlines off

	strip = line.rstrip()
	rest_rating = strip.split(":")
	rest_name, rest_rate = rest_rating
	rest_dict[rest_name] = rest_rate

rest_name = raw_input("Please enter the restaurant's name. >>> ")
rest_rate = int(raw_input ("Please enter the restaurant's rating. >>> "))
rest_dict[rest_name] = rest_rate
sorted_dict = sorted(rest_dict)	

for x in rest_dict:
	print "%s is rated at %s." % (x, rest_dict[x])
