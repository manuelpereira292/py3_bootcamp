#The takewhile module is basically the opposite of the 
# dropwhile iterator that we looked at earlier. 
# takewhile will create an iterator that returns 
# elements from the iterable only as long as our 
# predicate or filter is True. 

from itertools import takewhile

print(list(takewhile(lambda x: x<5, [1,4,6,4,1])))