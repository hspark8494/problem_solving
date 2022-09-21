li = []
sum = 0
for i in range(0,9):
    t = int(input())
    sum = sum+t
    li.append(t)

for i in li:
    for j in li:
        if i==j:
            continue
        if sum-i-j == 100:
            li.remove(i)
            li.remove(j)
            break
    if len(li) != 9:
        break

for i in sorted(li):
    print(i)