import sys
input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split(" "))
nodes = [i for i in range(n+1)]
def find(x):
    while x!=nodes[x]:
        nodes[x] = nodes[nodes[x]]
        x = nodes[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x<=y:
        nodes[y] = x
    else:
        nodes[x] = y

for _ in range(m):
    o, x, y = map(int, input().rstrip().split(" "))
    if o:
        print("YES\n" if find(x)==find(y) else "NO\n")
    else:
        union(x,y)