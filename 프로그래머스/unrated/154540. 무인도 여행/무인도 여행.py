import sys
sys.setrecursionlimit(100000)
pos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cnt = 0


def solution(maps: list):
    global cnt
    H, W = len(maps), len(maps[0])
    visited = [[False]*W for _ in range(H)]
    result = []

    def dfs(h, w):
        global cnt
        if visited[h][w]:
            return 0
        visited[h][w] = True
        if not maps[h][w].isnumeric():
            return 0
        cnt += int(maps[h][w])
        for p in pos:
            nh, nw = h+p[0], w+p[1]
            if H > nh >= 0 and W > nw >= 0 and not visited[nh][nw] and maps[nh][nw].isnumeric():
                dfs(nh, nw)

    for i in range(H):
        for j in range(W):
            if not visited[i][j]:
                dfs(i, j)
                if cnt != 0:
                    result.append(cnt)
                cnt = 0
    if not result:
        return [-1]
    else:
        return sorted(result)


print(solution(["1X1"]))
