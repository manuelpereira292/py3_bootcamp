from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('https://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass