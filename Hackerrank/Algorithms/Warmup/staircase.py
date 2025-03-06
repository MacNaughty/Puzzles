def staircase(n):
    if n == 0:
        return

    for i in range(n):
        print(''.join([' '] * (n - 1 - i)) + ''.join(['#'] * (i + 1)))



if __name__ == '__main__':
    staircase(6)
