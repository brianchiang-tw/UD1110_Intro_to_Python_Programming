# QUESTION 1 OF 5
# Use the code below to determine what will print to the console.

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

# What will happen when we run this code?

# Answer:
# It will print 'Variable scope is an important concept.'



# QUESTION 2 OF 5
# Now let's say we tweak the code a bit and comment out str1 = 'Variable scope is an important concept.'

str1 = 'Functions are important programming concepts.'

def print_fn():
    #str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()

# What will happen when we run this code?

# Answer:
# It will print 'Functions are important programming concepts.'



# QUESTION 3 OF 5
# We made another tweak to the code.

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn(str1)

# What do you think will happen when we run this code?

# Answer:
# It will give a TypeError: print_fn() takes 0 positional argument but 1 was given



# QUESTION 4 OF 5
# We made a final tweak to the code.

str1 = 'Functions are important programming concepts.'

def print_fn():
    print(str1)

print_fn(str1)
# Now what do you think will happen?

# Answer:
# It will give a TypeError: print_fn() takes 0 positional argument but 1 was given