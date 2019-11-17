# Q1:
#
# What happens when you call a string method like islower() on a float object? 
# For example, 13.37.islower().
# 
# There is a playground workspace further down this page that you can use to experiment.


# print( 13.37.islower() )

# expected output with an error message:
# AttributeError: 'float' object has no attribute 'islower'




# Q2:
# format() Practice
# Use the coding space below to practice using the format() string method. 
# 
# There are no right or wrong answers here, just practice!

greeting = "Hello world"
print (" Try formatting method, output {}".format(greeting) )