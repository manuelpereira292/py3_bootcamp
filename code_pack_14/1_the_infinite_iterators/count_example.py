#The count iterator will return evenly spaced values 
# starting with the number you pass in as its start
# parameter
from itertools import count

for i in count(10):
    if i > 20:
        break
    else:
        print(i)
