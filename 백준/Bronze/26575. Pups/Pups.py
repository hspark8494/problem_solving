import sys
input = sys.stdin.readline

for _ in range(int(input())):
    A, B, C = map(float, input().split(' '))
    print(f'${round(A*B*C, 2):.2f}')