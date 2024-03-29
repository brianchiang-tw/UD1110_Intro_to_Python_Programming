# Q1:
# Quiz: Zip Coordinates

# Use zip to write a for loop that creates a string specifying the label and coordinates 
# of each point and appends it to the list points. 
# 
# Each string should be formatted as label: x, y, z. 
# 
# For example, the string for the first coordinate should be F: 23, 677, 4.

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

parameter = list( zip(labels, x_coord, y_coord, z_coord)  )
points = []
# write your for loop here
for p in parameter:
    str_in_order = "{}: {}, {}, {}".format( p[0], p[1], p[2], p[3])
    points.append( str_in_order )


for point in points:
    print(point)

# expected output:
'''
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1
'''



# Q2:   
# Zip Lists to a Dictionary

# Use zip to create a dictionary cast that uses names as keys and heights as values.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict( zip(cast_names, cast_heights ))# replace with your code
print(cast)

# expected output:
'''
{'Ted': 72, 'Lily': 66, 'Marshall': 76, 'Robin': 68, 'Barney': 72}
'''



# Q3"
# Quiz: Unzip Tuples
# Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
(names, heights) = zip( *cast )

print(names)
print(heights)

# expected output:
'''
('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
(72, 68, 72, 66, 76)
'''



# Q4:
# Quiz: Transpose with Zip
# Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. 
# 
# There's actually a cool trick for this! Feel free to look at the solutions if you can't figure it out.

data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))


data_transpose = tuple( zip( *data ) )# replace with your code
print(data_transpose)

# expected output:
'''
((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))
'''



# Q5:
# Quiz: Enumerate
# Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, c in enumerate(cast):
    
    #print(i, c, heights[i] )
    cast[i] = str(c) + " " + str( heights[i] ) 

print(cast)

# expected output
'''
['Barney Stinson 72', 'Robin Scherbatsky 68', 'Ted Mosby 72', 'Lily Aldrin 66', 'Marshall Eriksen 76']
'''

