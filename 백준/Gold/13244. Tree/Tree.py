import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    M = int(input())
    parent = [i for i in range(N+1)]

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x==y:
            return True
        parent[y] = x
        return False

    flag = False
    for _ in range(M):
        x, y = map(int, input().rstrip().split(" "))
        flag = flag or union(x,y)

    if flag:
        print("graph")
    else:
        p = find(1)
        for i in range(1, N+1):
            if p != find(i):
                print("graph")
                break
        else:
            print("tree")
    