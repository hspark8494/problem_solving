ip =[]
while True:
    x = int(input())
    if x==0:
        break
    ip.append(x)

m = max(ip)
n = m*2
li = [i for i in range(n+1)]
li[1] = 0
for i,j in enumerate(li):
    if j != 0:
        x=2
        while i*x<len(li):
            li[i*x]=0
            x=x+1

for s in ip:
    c = 0
    for i in range(s+1,s*2+1):
        if li[i] !=0:
            c=c+1
    print(c)