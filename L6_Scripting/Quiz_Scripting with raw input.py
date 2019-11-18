
# get and process input for a list of names
input_str = input("Enter names separated by commas:")
names = input_str.split(",")

print( "names : {}".format( names) )


# get and process input for a list of the number of assignments
input_str = input("Enter assignment counts separated by commas:")
assignments =  list( map(int, input_str.split(",") ) )

print( "assignments : {}".format(assignments) )

# get and process input for a list of grades
input_str = input("Enter grades separated by commas:")
grades = list( map(int, input_str.split(",") ) )

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

for index in range( len(names) ):
    print( message.format( names[index], assignments[index], grades[index], grades[index]+2*assignments[index] ) )