import re, sys
input = sys.stdin.readline

N = int(input())
p = input().rstrip().replace("*", "[a-z]*")
r = re.compile(p)

for _ in range(N):
    s = input().rstrip()
    print("DA" if r.fullmatch(s) else "NE")