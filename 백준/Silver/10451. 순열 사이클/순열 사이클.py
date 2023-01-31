import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)


def dfs(i, li, visited):
    if visited[i] == True:
        return
    visited[i] = True
    dfs(li[i], li, visited)


for _ in range(int(input())):
    x = int(input())
    li = list(map(lambda x: int(x) - 1, input().rstrip().split(" ")))
    visited = [False] * x
    result = 0
    for i in range(x):
        if not visited[i]:
            result += 1
            dfs(i, li, visited)
    print(result)
