import sys

input = sys.stdin.readline

N = int(input())
li = [list(map(int, input().split(" "))) for _ in range(N)]

def find2(x1,x2,y1,y2):
    return sorted([x1,x2,y1,y2])[2]

while N>1:
    next = []
    for i in range(0, N//2):
        next.append([])
        x = i*2
        for j in range(0, N, 2):
            next[i].append(find2(li[x][j], li[x][j+1], li[x+1][j], li[x+1][j+1]))
    li = next
    N = N//2

print(li[0][0])
