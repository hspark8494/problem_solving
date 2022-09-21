import sys
n,c=map(int,input().split())
t=[0]*(c+1)
for _ in range(n):
    i=int(sys.stdin.readline())
    for j in range(i,c+1,i):
        t[j]=1
print(sum(t))