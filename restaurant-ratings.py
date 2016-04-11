# your code goes here
import sys # open the file 
import random

rest_dict = {} #define a dict
file_name = sys.argv[1]
file_data = open(file_name) # iterate and split data
new_rating = 0

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


#Greet the user and ask for their name
user_name = raw_input("Hi! What's your name? >>> ")
#Choose a random restaurant from the list in the file
while new_rating != "q":
	random_rest = random.choice(rest_dict.items())
	rest, rate = random_rest
	#Tell the user the chosen restaurant and its rating
	print "%s is rated at %s." % (rest, rate)
	#Ask the user what the new rating should be
	new_rating = raw_input("What should the new rating be? >>> ")
	#Update the rating
	rest_dict[rest] = new_rating
#Choose another restaurant, repeat steps 2-4

#Continue until the user types q.