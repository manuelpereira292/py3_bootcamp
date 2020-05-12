from functools import wraps

x = 11

def beg(target_function, a):

    @wraps(target_function)
    def wrapper(*args, **kwargs):
        if x > 10:
            raise Exception('Cant run')
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am thirsty :(")
        return msg
    return wrapper

@beg(a = 12)
def say(say_please = False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())
print(say(True))
