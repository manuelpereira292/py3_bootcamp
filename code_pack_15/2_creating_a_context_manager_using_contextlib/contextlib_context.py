from contextlib import contextmanager

@contextmanager
def file_open(path):
    try:
        f_obj = open(path, 'w')
        yield f_obj
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        f_obj.close()

if __name__ == '__main__':
    with file_open('code_pack_15/2_creating_a_context_manager_using_contextlib/test.txt') as fobj:
        fobj.write('Testing context managers')