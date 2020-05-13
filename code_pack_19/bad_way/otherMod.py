import logging

def add(x, y):
    """"""
    x+=1
    logging.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y