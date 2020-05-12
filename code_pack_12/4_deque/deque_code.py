from collections import deque
import argparse

def get_last(filename, n=2):
    """
    Returns the last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Error opening file: {}".format(filename))
        raise

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename')
    args = parser.parse_args()

    print(get_last(args.filename))

