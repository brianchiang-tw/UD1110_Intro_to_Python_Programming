# Quiz: Write a Docstring
# Write a docstring for the readable_timedelta function you defined earlier! 
# Remember the way you write your docstrings is pretty flexible! 
# Look through Python's docstring conventions here and check out this Stack Overflow page for some inspiration!


def readable_timedelta(days):
    # insert your docstring here
    
    '''
    Input: integer of days
    Output: string of conversion with week and remainder days
    '''
    
    
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)