N = int(input())
li = list(map(int, input().split(" ")))
r = []
curr = []
for i, val in enumerate(li):
    if i == 0:
        curr.append(val)
        continue
    if val > li[i-1]:
        curr.append(val)
    else:
        r.append(curr)
        curr = [val]
r.append(curr)

mx = 0
for li in r:
    if len(li) >= 2:
        mx = max(mx, li[-1] - li[0])
print(mx)