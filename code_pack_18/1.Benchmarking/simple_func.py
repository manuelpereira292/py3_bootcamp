# simple_func.py
def my_function():
    try:
        1 / 0
    except ZeroDivisionError:
        pass


#python -m timeit "import simple_func; simple_func.my_function()"
