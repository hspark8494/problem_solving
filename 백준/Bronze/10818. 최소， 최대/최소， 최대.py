input()
t = list(map(int, input().split()))
mx = -1000000
mn = 1000000

for i in t:
    if i>=mx:
        mx = i
    if i<=mn:
        mn = i

print(mn, mx)