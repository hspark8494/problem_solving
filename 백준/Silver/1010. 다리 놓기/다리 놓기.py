import math
for _ in range(int(input())):
    k,n=map(int,input().split())
    print(math.comb(n,k))