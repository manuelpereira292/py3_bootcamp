import sys

while True:
    print('PROGRAM: Type something, then hit Enter:')
    user_input = sys.stdin.readline().rstrip('\r\n')
    print('"PROGRAM: You typed: "' + user_input + '"')

    # user_input = input('-->PROGRAM: Type something, then hit Enter:')
    # print('"PROGRAM: You typed: "' + user_input + '"')