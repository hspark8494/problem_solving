import sys

input = sys.stdin.readline
N, P = map(int, input().split(" "))
nodes = [i for i in range(N+1)]
known = [False for i in range(N+1)]

l = list(map(int, input().split(" ")))

for x in range(l[0]):
    known[l[x+1]] = True

parties = [list(map(int, input().split(" "))) for _ in range(P)]
result = 0
for i in range(51):
    result = 0
    for party in parties:
        falg = False
        for i in range(party[0]):
            if known[party[i+1]]:
                falg = True
                break
        else:
            result+=1

        if falg:
            for i in range(party[0]):
                known[party[i+1]] = True

print(result)
