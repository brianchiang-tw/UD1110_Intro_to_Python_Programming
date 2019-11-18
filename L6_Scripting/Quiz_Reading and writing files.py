
# Q1:
# Use the relevant part of the Python documentation to find a method that reads the next line of a file. 
# Put the name of the method in the box.
#
# Python documentation:
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# Answer:
# readline()



# Q2:
# Flying Circus Cast List

# You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. 
# It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com). 
# 
# Each line of that file consists of an actor's name, a comma, and then some (messy) information about roles they played in the programme. 
# 
# You'll need to extract only the name and add it to a list. 
# You might use the .split() method to process each line.
import os

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    current_work_directory = os.path.dirname( os.path.abspath(__file__) )
    filename = current_work_directory + "\\" + filename

    with open(filename,'r') as f:
        
        for line in f:
            actor_name = line.split(",")[0]
            cast_list.append( actor_name )    
        

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')

for actor in cast_list:
    print(actor)


# expected output
'''
Graham Chapman
Eric Idle
Terry Jones
Michael Palin
Terry Gilliam
John Cleese
Carol Cleveland
Ian Davidson
John Hughman
The Fred Tomlinson Singers
Connie Booth
Bob Raymond
Lyn Ashley
Rita Davies
Stanley Mason
David Ballantyne
Donna Reading
Peter Brett
Maureen Flanagan
Katya Wyeth
Frank Lester
Neil Innes
Dick Vosburgh
Sandra Richards
Julia Breck
Nicki Howorth
Jimmy Hill
Barry Cryer
Jeannette Wild
Marjorie Wilde
Marie Anderson
Caron Gardner
Nosher Powell
Carolae Donoghue
Vincent Wong
Helena Clayton
Nigel Jones
Roy Gunson
Daphne Davey
Stenson Falke
Alexander Curry
Frank Williams
Ralph Wood
Rosalind Bailey
Marion Mould
Sheila Sands
Richard Baker
Douglas Adams
Ewa Aulin
Reginald Bosanquet
Barbara Lindley
Roy Brent
Jonas Card
Tony Christopher
Beulah Hughes
Peter Kodak
Lulu
Jay Neill
Graham Skidmore
Ringo Starr
Fred Tomlinson
David Hamilton
Suzy Mandel
Peter Woods
'''