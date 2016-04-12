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

try:
	rest_rate = int(raw_input ("Please enter the restaurant's rating. >>> "))
except ValueError:
	rest_rate = int(raw_input ("Sorry, wrong format. Try again with a number? >>> "))

rest_dict[rest_name.capitalize()] = rest_rate
#sorted_dict = sorted(rest_dict)	

for x in sorted(rest_dict):
	print "%s is rated at %s." % (x, rest_dict[x])


#Greet the user and ask for their name
user_name = raw_input("Anyway, hi! What's your name? >>> ")
#Choose a random restaurant from the list in the file
while new_rating != "q":
	random_rest = random.choice(rest_dict.items())
	rest, rate = random_rest
	#Tell the user the chosen restaurant and its rating
	print "%s is rated at %s." % (rest, rate)

		# Ask the user what the new rating should be
	try:
		user_name = user_name.capitalize()
		new_rating = raw_input("So {}, what should the new rating be? >>> ".format(user_name))
		if new_rating == "q":
			break
		else:
			rest_dict[rest] = int(new_rating)
	except ValueError:
		user_name = user_name.capitalize()
		print "Sorry {}, wrong format. Try again with a number? >>> ".format(user_name)
		continue

#Choose another restaurant, repeat steps 2-4
# sorted_dict = sorted(rest_dict)	
for x in sorted(rest_dict):
	print "%s is rated at %s." % (x, rest_dict[x])
#Continue until the user types q.