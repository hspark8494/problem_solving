#
# 분리 집합 Union-Find 
#
# find(x) : 노드 x가 속한 집합의 최상위 노드를 반환
# union(x, y) : x, y를 하나의 집합으로 병합 
#

def find(x):
    while x!=parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x!=y:
        parents[y] = x
        return True
    else:
        return False

N = 1000
parents = [i for i in range(N+1)]