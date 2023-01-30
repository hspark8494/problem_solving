x = int(input())

l = list(map(int, input().split(" ")))
r = 0
for i in l:
    r += min(x, i)
print(r)