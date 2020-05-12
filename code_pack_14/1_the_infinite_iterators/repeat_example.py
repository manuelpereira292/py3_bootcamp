# The repeat iterators will return an object an object over 
# and over again forever unless you set its times argument
from itertools import repeat

iterator = repeat(5, 5)
print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#5

print (next(iterator))
#error StopIteration
