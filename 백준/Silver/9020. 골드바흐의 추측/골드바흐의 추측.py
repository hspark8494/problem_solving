from sys import stdin
input = stdin.readline

que = [int(input()) for _ in range(int(input()))]
mx = max(que)
seive = [i%2!=0 for i in range(mx+1)]
seive[1] = False
seive[2] = True
li = [2]
for i in range(3, mx+1):
    if seive[i]:
        li.append(i)
        for j in range(i*i, mx+1, i):
            seive[j] = False

for n in que:
    a, b = 0, 0
    while li[a]<n//2:
        a+=1
    b = a
    while True:
        curr = li[a] + li[b]
        if li[a] + li[b] == n:
            print(li[a], li[b])
            break
        elif curr > n:
            a-=1
        else:
            b+=1
