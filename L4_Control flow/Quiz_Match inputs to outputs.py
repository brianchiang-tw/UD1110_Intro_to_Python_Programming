# Q1:
# Practice with range
# For each below, match the input code to the appropriate output.


# [0, 1, 2, 3]
print(list(range(4)))

# [4, 5, 6, 7]
print(list(range(4,8)))

# [4, 6, 8]
print(list(range(4,10,2)))

# []
# Remember that range is tail-exclusive, and default step value = +1 (offset per round)
print(list(range(0,-5)))



# Q2:
# Use the code below to complete the next quiz.

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part

    lower_colors.append( color.lower() )


print( lower_colors )