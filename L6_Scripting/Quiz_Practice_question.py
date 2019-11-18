# Write your code here
import os

filename = os.path.dirname( os.path.abspath( __file__ ) ) + "\\" + "flowers.txt"

flower_dict = dict()

with open(filename,'r') as f:
    for line in f:
        token = list( line.split(" ") )

        letter_index = token[0][0].lower()
        flower_name = token[1]
        # print( letter_index )
        # print( flower_name )
        flower_dict[ letter_index ] = flower_name



# HINT: create a dictionary from flowers.txt

# HINT: create a function to ask for user's first and last name
str_input = input("Enter your First [space] Last name only: \nFor example, Bill Newman\n")
print("Unique flower name with the first letter: {}".format( flower_dict[ str_input[0].lower() ] ) )

# print the desired output