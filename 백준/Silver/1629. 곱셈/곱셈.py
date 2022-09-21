import sys

def product(a, b, c):
    if b==1:
        return a % c
    else:
        d = product(a, b//2, c)
        if b%2==0:
            return (d * d) % c
        else:
            return (d * d * a) % c

input = sys.stdin.readline
A, B, C = map(int, input().split(" "))

print(product(A,B,C))