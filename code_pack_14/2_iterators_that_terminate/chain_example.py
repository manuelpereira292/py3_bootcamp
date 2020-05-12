#The chain iterator will take a series of iterables 
# and basically flatten them down into one long iterable
from itertools import chain

my_list = ['foo', 'bar']
numbers = list(range(5))
cmd = ['ls', '/some/dir']

my_list = list(chain(['foo', 'bar'], cmd, numbers))
print(my_list)
