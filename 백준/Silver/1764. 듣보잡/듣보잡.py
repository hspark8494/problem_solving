import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))
s1 = set()
s2 = set()
for _ in range(n):
    s1.add(input().rstrip())
for _ in range(m):
    s2.add(input().rstrip())

result = sorted(list(s1 & s2))

print(len(result))
print(*result, sep="\n")