# Q1:
# Quiz: Extract First Names
# Use a list comprehension to create a new list first_names 
# containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# write your list comprehension here
first_names = [ x.split()[0].lower() for x in names ]
print(first_names)

# expected output
'''
['rick', 'morty', 'summer', 'jerry', 'beth']
'''



# Q2:
# Quiz: Multiples of Three
# Use a list comprehension to create a list multiples_3 containing the first 20 multiples of 3.

# write your list comprehension here
multiples_3 = [ (x*3) for x in range(1, 21)]

print(multiples_3)

# expected output:
'''
[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
'''



# Q3:
# Quiz: Filter Names by Scores
# Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# write your list comprehension here
passed = [ student for student, grade in scores.items() if grade > 65 ]

print(passed)

# expected output:
'''
['Rick Sanchez', 'Beth Smith', 'Summer Smith']
'''