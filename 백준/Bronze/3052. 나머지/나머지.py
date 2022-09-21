l = [int(input())%42 for i in range(10)]

n = 1

for i in range(10):
    for j in range(10):
        if i==j or l[j] == -1:
            continue
        if l[j] == l[i]:
            l[i] = -1
            break
        if j >= 9:
            n = n+1

print(n)