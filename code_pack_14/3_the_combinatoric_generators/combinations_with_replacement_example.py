from itertools import combinations_with_replacement

for item in combinations_with_replacement('01', 32):
    print(''.join(item))