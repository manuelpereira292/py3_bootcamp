#The compress sub-module is useful for filtering the 
# first iterable with the second. 

from itertools import compress


letters = 'ABCDEFG'
bools = [True, False, True, True, False]
print(list(compress(letters, bools)))
