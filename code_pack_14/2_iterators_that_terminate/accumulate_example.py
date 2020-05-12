#The accumulate iterator will return accumulated sums 
# or the accumulated results of a two argument function 
# that you can pass to accumulate.

from itertools import accumulate

print(list(range(10)))
print(list(accumulate(range(10))))
