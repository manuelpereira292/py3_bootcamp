li = [1,2,3]
li += [4, 5, 6]
print(li)

li = [1,2,3]
li = li + [4, 5, 6]
print(li)
print('--------------------------------------')


from functools import partial

def add(x,y):
    return 2*x + y

p2 = partial(add, 1,2)
print(p2())
print(p2())
print(p2())

p1 = partial(add, y=1)
print(p1(5))
print(p1(7))