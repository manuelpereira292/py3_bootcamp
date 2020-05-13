def doubler(x):
    return x * 2

my_list = [1, 2, 3, 4, 5]
for item in map(doubler, my_list):
    print(item)

def add(x, y):
    return x + y

my_list1 = [1, 3]
my_list2 = [2, 4]
for item in map(add, my_list1, my_list2):
    print(item)