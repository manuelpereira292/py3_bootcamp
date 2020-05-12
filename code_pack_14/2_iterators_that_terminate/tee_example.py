#The tee will create n iterators from a single iterable. 

from itertools import tee

data = 'ABCDE'
iter1, iter2 = tee(data)

for item in iter1:
    print(item)

for item in iter2:
    print(item)



data = 'FGHI'
iter1, iter2, iter3 = tee(data,3)

for item in iter1:
    print(item)

for item in iter2:
    print(item)

for item in iter3:
    print(item)