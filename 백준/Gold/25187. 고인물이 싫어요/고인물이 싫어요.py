import sys
sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, M, X = map(int, input().rstrip().split(" "))
nodes = [[] for _ in range(N+1)]
state = [0] + list(map(int, input().rstrip().split(" ")))

for _ in range(M):
    p, q = map(int, input().rstrip().split(" "))
    nodes[p].append(q)
    nodes[q].append(p)

def dfs(i, visited, buffer):
    global result
    if visited[i]:
        return
    if state[i]:
        result += 1
    else:
        result -= 1
    visited[i] = True
    buffer.append(i)
    for next in nodes[i]:
        if not visited[next]:
            dfs(next, visited, buffer)

visited = [False for _ in range(N+1)]
for i in range(1,N+1):
    if not visited[i]:
        result = 0
        buffer = []
        dfs(i, visited, buffer)
        result = int(result>0)
        for x in buffer:
            state[x] = result

for _ in range(X):
    print(state[int(input())])