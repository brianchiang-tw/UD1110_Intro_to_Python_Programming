# Practice_#1
# Quick Brown Fox

# Use a for loop to take a list and print each element of the list in its own line.


sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]


# Method_#1
for word in sentence:
    print(word)


# Method_#2
'''
for index in range(0, len(sentence) ):
    print( sentence[index] )
'''



# Practice_#2
# Multiples of 5
# Write a for loop below 
# that will print out every whole number that is a multiple of 5 and less than or equal to 30.

for number in range( 5, 31, 5):
    print(number)