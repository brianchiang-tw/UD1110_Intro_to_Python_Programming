
# Q1:
# The following are some common exceptions. 
# Again, "exceptions" are errors detected during execution. 
# 
# See if you can recall and match each error with its meaning and the steps you will take to handle the exception. 
# If you need help, feel free to do some research online to learn more about the exception.

# NameError: name 'abc_dict' is not defined
# => You are trying to access a local variable before it is denied. 
# => Make sure local scope of variable in function is defined or value assigned to it.

# UnboundLocalError
# => Identifier is not found in the local or global namespace. 
# => Make sure the reference to the identifier is corretly added to the code.

# ValueError: too many values to unpack (expected 2)
# => Assignation error. Inconsistency in how many values being unpacked and how many vriables the values should be assigned to.

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# => An operation or function is applied to an object of inappropriate type - e.g., trying to concatenate a string and integer. Change the datatype for one of the values (e.g., change int ot str)



# Q2:
# Practice Debugging
# In the workspace at the bottom of the page, there is a piece of code in the user_input_numlist.py Python file. The code prompts the user to enter 10 two-digit numbers. It should then find and print the sum of all of the even numbers among those that were entered.

# But there is a bug in the code! When I input a number, I get the following TypeError. Use the programming environment provided below with a Terminal and code editor to debug the code.

# initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    
# check to see if number is even and if yes, add to list_sum
# print incorrect value warning  when ValueError exception occurs
    try:
        number = int(userInput)
        user_list.append(number)
        if number % 2 == 0:
            list_sum += number
    except ValueError:
        print("Incorrect value. That's not an int!")

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))