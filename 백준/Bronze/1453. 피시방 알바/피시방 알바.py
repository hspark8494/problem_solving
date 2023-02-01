input()
r = 0
s = set()
for i in map(int, input().split(" ")):
    if i in s:
        r += 1
    else:
        s.add(i)
print(r)