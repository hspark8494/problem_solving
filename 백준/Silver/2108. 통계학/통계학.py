from sys import stdin
l = []
for _ in range(int(input())):
	l.append(int(stdin.readline()))
	
l.sort()

print(int(round(sum(l)/len(l))))
print(l[len(l)//2])

t = [[l[0],0]]

for i in l:
    if t[-1][0] == i:
        t[-1][1] += 1
    else:
        t.append([i,1])

t.sort(key=lambda x:(-x[1],x[0]))

if len(t)>1 and t[0][1]==t[1][1]:
    print(t[1][0])
else:
    print(t[0][0])

print(l[-1]-l[0])