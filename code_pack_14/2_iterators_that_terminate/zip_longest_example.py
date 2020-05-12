#The zip_longest iterator can be used to zip 
# two iterables together. 
from itertools import zip_longest

for item in zip_longest('ABCD', 'xy', fillvalue='BLANK'):
    print (item)


for item in zip('ABCD', 'xy'):
    print (item)