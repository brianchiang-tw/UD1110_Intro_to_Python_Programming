# Q1: 
# Create Usernames

# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores. Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# should create the list:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

# HINT: Use the .replace() method to replace the spaces with underscores. 
# Check out how to use this method in this Stack Overflow answer.


for name in names:

    # convert to lowercase letter
    lowercase_name = name.lower()

    # repalce white space ' ', with underline '_'
    name_with_underline = lowercase_name.replace(" ", "_")

    # add to list unsernames
    usernames.append( name_with_underline )

print(usernames)    



#Q2:
# Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?


names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
         name = name.lower().replace(" ", "_")

print(names)

# Answer:
# The printed output for the names list will look exactly like it did in the first line. 
# During each iteration, the name variable is set to a string taken from the list. 
# Then the assignment statement creates a new string (name.lower().replace(" ", "_")) and 
# changes the name variable to that string. 
# 
# It doesn't modify the contents of the names list at all. 
# 
# To modify the list you must operate on the list itself, using range, as you saw earlier.



#Q3:
# Modify Usernames with Range

# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores. After running your loop, this list

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# should change to this:

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

for index in range ( 0, len(usernames) ):

    # carry out conversion
    name_conversion = usernames[ index ].lower().replace(" ", "_")

    # update to list element with index
    usernames[ index ] = name_conversion

print(usernames)



#Q4:
# Tag Counter

# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. 
# XML is a data language similar to HTML. 
# 
# You can tell if a string is an XML tag 
# if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
# 
# Keep track of the number of tags using the variable count.

# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == "<" and token[-1] == ">":
        
        # update counter if we meet an XML tag, enclosed by caret pair <>
        count += 1


print(count)



#Q5:
# Create an HTML List
# Write some code, 
# including a for loop, that iterates over a list of strings and creates a single string, 
# html_str, which is an HTML list. 
# 
# For example, if the list is items = ['first string', 'second string'], 
# printing html_str should output:

'''
<ul>
<li>first string</li>
<li>second string</li>
</ul>
'''

# That is, the string's first line should be the opening tag <ul>. 
# 
# Following that is one line per element in the source list, surrounded by <li> and </li> tags. 
# 
# The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    
    # generate html code per item
    html_code = "<li>" + item + "</li>\n"
    
    # padding to html string
    html_str = html_str + html_code
    
# for adding last </ul>
html_str += "</ul>"


print(html_str)