import math
import sys
input = sys.stdin.readline

N = 1
while True:
    O, W = map(int, input().rstrip().split(" "))
    if O == 0 and W == 0:
        break
    while True:
        op, val = input().rstrip().split(" ")
        val = int(val)
        if op == 'E' and W > 0:
            W -= val
        elif op == 'F' and W > 0:
            W += val
        elif op == '#':
            break
    if O*2 > W > O//2:
        print(N, ':-)')
    elif W <= 0:
        print(N, 'RIP')
    else:
        print(N, ':-(')
    N += 1
