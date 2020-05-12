#The starmap tool will create an iterator that can 
# compute using the function and iterable provided.

from itertools import starmap

def add(a, b):
    return a+b

for item in starmap(add, [(2,3), (4,5)]):
    print(item)