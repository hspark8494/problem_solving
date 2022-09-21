from sys import stdin
li = [int(stdin.readline()) for _ in range(int(stdin.readline()))]
print(*sorted(li,reverse=True), sep="\n")