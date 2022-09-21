import sys
N, K = map(int, input().split())

seive = [True for _ in range(N+1)]

for i in range(2, N+1):
    if seive[i]:
        for j in range(i, N+1, i):
            if seive[j]:
                seive[j] = False
                K-=1
                if K <=0 :
                    print(j)
                    sys.exit()