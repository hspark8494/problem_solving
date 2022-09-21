import sys

lines = sys.stdin.readlines()
idx = 1
for i in range(int(lines[0])):
    N, M = map(int, lines[idx].rstrip().split(" "))
    idx+=M+1
    print(N-1)