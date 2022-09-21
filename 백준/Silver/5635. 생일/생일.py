l = []
for _ in range(int(input())):
    l.append(input().split())

l.sort(key=lambda x : (int(x[3]), int(x[2]), int(x[1])))
print(l[-1][0],l[0][0])