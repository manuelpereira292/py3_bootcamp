#The cycle iterator from itertools allows you to 
# create an iterator that will cycle through a series 
# of values infinitely. 

from itertools import cycle

count = 0

for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1
