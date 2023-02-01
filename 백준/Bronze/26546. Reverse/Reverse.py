import sys
input = sys.stdin.readline

for _ in range(int(input())):
    S, start, end = input().rstrip().split(" ")
    start, end = int(start), int(end)
    print(S[:start] + S[end:])
