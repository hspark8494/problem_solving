from sys import stdin
input = stdin.readline

def dfs(i, nodes, visited, result, pre):
    if visited[i]:
        result[-1] = False
        return
    visited[i] = True
    for next in nodes[i]:
        if next != pre:
            dfs(next, nodes, visited, result, i)
X = 1

while X:
    E, V = map(int, input().split(" "))
    if E==0 and V==0:
        break

    nodes = [[] for _ in range(E+1)]
    visited = [0 for _ in range(E+1)]

    for _ in range(V):
        e1, e2 = map(int, input().split(" "))
        nodes[e1].append(e2)
        nodes[e2].append(e1)
    
    result = []

    for i in range(1, E+1):
        if not visited[i]:
            result.append(True)
            dfs(i, nodes, visited, result, None)

    r = sum(result)

    if r>1:
        print(f"Case {X}: A forest of {r} trees.")
    elif r==1:
        print(f"Case {X}: There is one tree.")
    else:
        print(f"Case {X}: No trees.")

    X+=1