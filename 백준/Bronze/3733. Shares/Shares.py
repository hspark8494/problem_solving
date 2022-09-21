from sys import stdin
lines = stdin.readlines()
for line in lines:
    N, S = map(int, line.rstrip().split(" "))
    print(S//(N+1))