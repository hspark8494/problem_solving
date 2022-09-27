def find(x):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parents[y] = x
        return True
    else:
        return False


N = 1000
parents = [i for i in range(N+1)]
