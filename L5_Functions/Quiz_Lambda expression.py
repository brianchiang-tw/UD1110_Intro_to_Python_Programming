# Q1:
# Quiz: Lambda with Map
# map() is a higher-order built-in function that takes a function and iterable as inputs, 
# and returns an iterator that applies the function to each element of the iterable. 
# 
# The code below uses map() to find the mean of each list in numbers to create the list averages. 
# Give it a test run to see what happens.

# Rewrite this code to be more concise by replacing the mean function 
# with a lambda expression defined within the call to map().



numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map( mean, numbers))
print(averages)


average = list( map( lambda x: sum(x)/len(x), numbers) )
print( average )

# expected output:
'''
[57.0, 58.2, 50.6, 27.2]
[57.0, 58.2, 50.6, 27.2]
'''



# Q2:
# Quiz: Lambda with Filter
# filter() is a higher-order built-in function that takes a function and iterable 
# as inputs and returns an iterator with the elements from the iterable 
# for which the function returns True. 
# 
# The code below uses filter() to get the names in cities 
# that are fewer than 10 characters long to create the list short_cities. 
# 
# Give it a test run to see what happens.

# Rewrite this code to be more concise 
# by replacing the is_short function with a lambda expression defined within the call to filter().


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

short_cities = list( filter( lambda city_name: len(city_name)<10, cities) )
print( short_cities )

# expected output:
'''
['Chicago', 'Denver', 'Boston']
['Chicago', 'Denver', 'Boston']
'''