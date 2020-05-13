#first
# from contextlib import redirect_stdout
# help(redirect_stdout)

#then
from contextlib import redirect_stdout

path = 'text.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)