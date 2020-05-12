#generator function requires Python’s yield statement

def doubler_generator():
    number = 2
    while True:
        yield number
        number *= number

doubler = doubler_generator()
print (next(doubler))
#2

print (next(doubler))
#4

print (next(doubler))
#16

print (type(doubler))
#<class 'generator'>
