import sys
a, p = map(int, input().split(" "))

li = [a]
s = set()
s.add(a)

while True:
    curr = 0
    for c in str(li[-1]):
        curr += (int(c) ** p)
    if curr in s:
        result = 0
        for i in range(len(li)-1, -1, -1):
            s.remove(li[i])
            if curr == li[i]:
                print(len(s))
                sys.exit()
    li.append(curr)
    s.add(curr)
