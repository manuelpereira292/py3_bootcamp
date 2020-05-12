from collections import Counter

counter_one = Counter('superfluous')
print (counter_one)

counter_two = Counter('super')
print(counter_one.subtract(counter_two))

print (counter_one)


#Counter({'u': 3, 's': 2, 'l': 1, 'r': 1, 'e': 1, 'o': 1, 'p': 1, 'f': 1})
#None
#Counter({'u': 2, 'l': 1, 'o': 1, 's': 1, 'f': 1, 'r': 0, 'e': 0, 'p': 0})