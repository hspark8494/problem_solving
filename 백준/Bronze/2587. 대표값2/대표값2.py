li = []
for i in range(5):
    li.append(int(input()))

li = sorted(li)
t = 0

for i in li:
    t=t+i

print(int(t/5))
print(li[2])