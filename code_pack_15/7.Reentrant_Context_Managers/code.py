#first
from contextlib import contextmanager
@contextmanager
def single():
    print('Yielding')
    yield
    print('Exiting context manager')
context = single()
with context:
    pass

#Yielding
#Exiting context manager

with context:
    pass

#-----Error

#then -  this works because redirect_stdoutput is reentrant
from contextlib import redirect_stdout
from io import StringIO
stream = StringIO()
write_to_stream = redirect_stdout(stream)
with write_to_stream:
    print('Write something to the stream')
    with write_to_stream:
        print('Write something else to stream')

print(stream.getvalue())
#Write something to the stream
#Write something else to stream