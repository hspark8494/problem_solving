import sys

input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split(" "))

parents = [[] for _ in range(N+1)]
childern = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
vaildate = [False for _ in range(N+1)]

for _ in range(M):
    p1, p2 = map(int, input().rstrip().split(" "))
    childern[p1].append(p2)
    parents[p2].append(p1)

for _ in range(K):
    o, idx = map(int, input().rstrip().split(" "))
    if o == 1:
        if vaildate[idx] or all([visited[i] >= 1 for i in parents[idx]]):
            vaildate[idx] = True
            visited[idx] += 1
            continue
    elif o == 2:
        if visited[idx] >= 1:
            visited[idx] -= 1
            if visited[idx] <= 0:
                for next in childern[idx]:
                    vaildate[next] = False
            continue
    print("Lier!")
    break
else:
    print("King-God-Emperor")
