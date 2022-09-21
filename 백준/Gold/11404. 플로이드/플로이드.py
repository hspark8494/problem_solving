import sys
input = sys.stdin.readline

V, E = int(input()), int(input())
graph = [[sys.maxsize if i!=j else 0 for j in range(V)] for i in range(V)]

for _ in range(E):
    l = list(map(int, input().split()))
    graph[l[0]-1][l[1]-1] = min(graph[l[0]-1][l[1]-1], l[2])

for k in range(V):
    for i in range(V):
        for j in range(V):
            if(graph[i][k] + graph[k][j] < graph[i][j]):
                graph[i][j] = graph[i][k] + graph[k][j]

for g in graph:
    print(*map(lambda x: 0 if x==sys.maxsize else x, g))