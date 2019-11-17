# Q1:

# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. I've included two test cases that you can use to verify that your function works correctly. Once you've written your function, use the Test Run button to test your code.

# write your function here
def population_density( people, area):
    
    density = people / area
    return density



# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# expected output:
'''
expected result: 10, actual result: 10.0
expected result: 7123.6902801, actual result: 7123.690280065897
'''



# Q2:
# Quiz: readable_timedelta
# Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

# print(readable_timedelta(10))
# should output the following:

# 1 week(s) and 3 day(s).

# write your function here
def readable_timedelta( days ):
    week = days // 7
    remaining = days % 7
    
    message = "{} week(s) and {} day(s).".format(week, remaining)
    #print( "{} week(s) and {} day(s).".format(week, remaining) )
    return message

# test your function
print(readable_timedelta(1))

# expected output
'''
1 week(s) and 3 day(s).
'''