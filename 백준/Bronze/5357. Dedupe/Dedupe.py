import sys
input = sys.stdin.readline

for _ in range(int(input())):
    pre, acc = '', ''
    for c in input().rstrip():
        if pre != c:
            acc += c
        pre = c
    print(acc)