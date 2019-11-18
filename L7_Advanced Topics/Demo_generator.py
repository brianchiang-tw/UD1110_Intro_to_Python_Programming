sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

print( sq_list )

print( sq_iterator )

print( list(sq_iterator) )

# expected output:
'''

[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
<generator object <genexpr> at 0x00000...some memory location>
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

'''