r = int(input()) * int(input()) * int(input())
a = [0] * 10

for c in str(r):
    a[int(c)] += 1

print(*a, sep="\n")