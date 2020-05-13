#first
#with open('code_pack_15/4_contextlib_suppress(exceptions)/fauxfile.txt') as fobj:
#    for line in fobj:
#        print(line)

#then     
from contextlib import suppress
with suppress(FileNotFoundError):
    with open('code_pack_15/4_contextlib_suppress(exceptions)/fauxfile.txt') as fobj:
        for line in fobj:
            print(line)
