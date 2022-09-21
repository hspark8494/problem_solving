from sys import stdin
l = []
for _ in range(int(input())):
    l.append(stdin.readline().split())
l.sort(key=lambda x: (-int(x[1]),x[0]))

print(l[0][0])