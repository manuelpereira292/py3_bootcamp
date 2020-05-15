# create folder
# arg_demo.py

import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()

#python arg_demo.py -h

#----------------------------------------------------------
# arg_demo2.py

import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    # required argument
    parser.add_argument('-x', action="store", required=True,
                        help='Help text for option X')
    # optional arguments
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()

# mike@pc:~/py/argsparsing$ python arg_demo2.py
# usage: arg_demo2.py [-h] -x X [-y Y] [-z Z]
# arg_demo2.py: error: argument -x is required

# mike@pc:~/py/argsparsing$ python arg_demo2.py -x something
# Namespace(x='something', y=False, z=None)

# mike@pc:~/py/argsparsing$ python arg_demo2.py -x something -y text
# Namespace(x='something', y='text', z=None)

# mike@pc:~/py/argsparsing$ python arg_demo2.py -x something -z text
# usage: arg_demo2.py [-h] -x X [-y Y] [-z Z]
# arg_demo2.py: error: argument -z: invalid int value: 'text'

# mike@pc:~/py/argsparsing$ python arg_demo2.py -x something -z 10
# Namespace(x='something', y=False, z=10)

#----------------------------------------------------------
#Short Options and Long Options
parser.add_argument('-x', action="store", required=True,
                    help='Help text for option X')

parser.add_argument('-x', '--execute', action="store", required=True,
                    help='Help text for option X')                        

#----------------------------------------------------------
#Options that Conflict
import argparse


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store",
                        help='Help text for option X')
    group.add_argument('-y', help='Help text for option Y', default=False)

    parser.add_argument('-z', help='Help text for option Z', type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()

# usage: arg_demo3.py [-h] [-x EXECUTE | -y Y] [-z Z]
# arg_demo2.py: error: argument -y: not allowed with argument -x/--execute    