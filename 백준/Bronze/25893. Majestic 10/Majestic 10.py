import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip().split(" ")
    lf = len(list(filter(lambda x: int(x) >= 10, s)))
    print(*s)
    print(['zilch', 'double', 'double-double', 'triple-double'][lf], '\n')