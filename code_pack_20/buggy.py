import sys 

def main():
    try:
        n = int(sys.argv[1])
    except:
        n=5
    matrix = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            matrix[i][j] = i*n + j + 1
    print('\n'.join([' '.join(['{:2d}'.format(e) for e in row]) for row in matrix]))
    return 0

main()
