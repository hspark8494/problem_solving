t, mx = 0, -1

for i in range(1, 10):
    j = int(input())
    if j>=mx:
        mx = j
        t = i

print(mx)
print(t)