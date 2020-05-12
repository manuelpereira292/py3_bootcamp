#Basically islice does is take a slice by index of your 
# iterable and returns the selected items as an iterator

from itertools import count, islice

for i in islice(count(), 3, 15):
    print(i)
