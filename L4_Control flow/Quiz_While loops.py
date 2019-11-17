# Q1:
# Quiz: Count By

# Suppose you want to count from some number start_num by another number count_by 
# until you hit a final number end_num. 
# 
# Use break_num as the variable that you'll change each time through the loop. 
# For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

# Before the loop, 
# what do you want to set break_num equal to? How do you want to change break_num each time through the loop? 
# What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, 
# showing the value that indicated it was time to stop looping. 
# 
# It is the case that break_num should be a number that is the first number larger than end_num.

start_num = 1 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 5 #provide some number to count by 

break_num = start_num
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while( break_num < end_num ):
    break_num += count_by

print(break_num)



# Q2:
# Quiz: Count By Check

# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, 
# and calculate break_num the way you did in the last quiz.

# Now in addition, 
# address what would happen if someone gives a start_num that is greater than end_num. 
# 
# If this is the case, set result to "Oops! Looks like your start value is greater than the end value. 
# 
# Please try again." Otherwise, set result to the value of break_num.

start_num = 1 #provide some start number
end_num = 101 #provide some end number that you stop when you hit
count_by = 3  #provide some number to count by 

break_num = start_num

# write a condition to check that end_num is larger than start_num before looping
# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

if start_num > end_num:
    error_msg = "Oops! Looks like your start value is greater than the end value. Please try again."
    print( error_msg )

while break_num < end_num :
    
    break_num += count_by

result = break_num
print(result)



# Q3:
# Quiz: Nearest Square

# Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. 
# 
# A square number is the product of an integer multiplied by itself, 

# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here

square = 1
i = 1

while square <= limit:

    # keep nrearest value per iteration
    nearest_square = square
    
    # increment i
    i += 1
    
    # update i square
    square = i ** 2


print(nearest_square)