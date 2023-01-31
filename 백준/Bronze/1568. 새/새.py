N = int(input())
t = 0
while N>0:
    for i in range(1, N+1):
        if i>N:
            break
        N-=i
        t+=1
print(t)