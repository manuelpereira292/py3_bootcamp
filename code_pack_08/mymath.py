def add(a,b):
    """
    Return the addition of the arguments: a +b
    
    >>> add(1,2)
    3
    >>> add(-1,10)
    9
    >>> add('a','b')
    'ab'
    >>> add(1,'2')
    Traceback (most recent call last):
      File 'mymath.py', line 15, in add
        return a + b
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    
    return a + b

if __name__ == '__main__':
    # x=1
    # y=2
    print(add(1,3)) # 3
    import doctest
    doctest.testmod()

#python mymath.py -v