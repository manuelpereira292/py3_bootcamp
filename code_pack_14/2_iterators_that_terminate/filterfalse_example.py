#The filterfalse function from itertools is very similar 
# to dropwhile. 
# However instead of dropping values that match True, 
# filterfalse will only return those values that evaluated 
# to False.

from itertools import filterfalse

def greater_than_five(x):
    return x > 5

print(list(filterfalse(greater_than_five, [6, 7, 8, 9, 1, 2, 3, 10])))
