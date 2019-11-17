# Q1:

# There are certain requirements you want to consider adding into a while loop. 
# Which of these requirements must be met? (Select all that apply)

# Answer

# (v) The condition for exiting the while loop should be included

# (v) Check if the iteration condition is met

# (v) Body of the loop should change the value of condition variables



# Q2:
# Question: What type of loop should we use?
# You need to write a loop that takes the numbers in a given list named num_list:
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

# Would you use a while or a for loop to write this code?

# We have provided our solution on the next page. Feel free to use the coding playground below to test your code.

## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_number_count = 0
index = 0
sum_value = 0

while odd_number_count <= 4:
    
    currnet_number = num_list[index]
    
    if currnet_number % 2== 1:
        
        # update sum
        sum_value += currnet_number
        
        # update odd_number_count
        odd_number_count += 1
        
    # update index for num_list iteration
    index += 1
        
    
print( "sum of first five odd numbers: {}".format(sum_value ) )   
print()


# verification by automation

odd_num = list( [ x for x in num_list if x % 2 == 1] )
print( "odd number array: {}".format( odd_num ) )

first_five_odd_nums = map( int, odd_num[0:5] )
print( "sum of first five odd numbers: {}".format( sum( first_five_odd_nums ) ) )