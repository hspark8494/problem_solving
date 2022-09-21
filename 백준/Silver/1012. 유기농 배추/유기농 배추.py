import sys
sys.setrecursionlimit(100000)
for _ in range(int(input())):
    x,y,n = map(int, input().split(" "))
    li = [[False for _ in range(y)] for _ in range(x)]
    visited = [[False for _ in range(y)] for _ in range(x)]
    result = 0
    for _ in range(n):
        i, j = map(int, input().split(" "))
        li[i][j] = True

    def dfs(i,j):
        try:
            if visited[i][j] or not li[i][j] or i<0 or j<0:
                return
        except:
            return
        visited[i][j] = True
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    for i in range(x):
        for j in range(y):
            if li[i][j] and not visited[i][j]:
                result+=1
                dfs(i,j)
    print(result)
