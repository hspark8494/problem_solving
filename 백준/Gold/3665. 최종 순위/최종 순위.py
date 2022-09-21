from collections import deque
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    nodes = [set() for _ in range(N+1)]
    degrees = [0 for _ in range(N+1)]
    li = list(map(int, input().rstrip().split(" ")))

    for i in range(0, len(li)-1):
        for j in range(i+1, len(li)):
            nodes[li[i]].add(li[j])
            degrees[li[j]] += 1

    M = int(input())
    for _ in range(M):
        p1, p2 = map(int, input().rstrip().split(" "))
        if p2 in nodes[p1]:
            p1, p2 = p2, p1
        nodes[p2].remove(p1)
        nodes[p1].add(p2)
        degrees[p2] += 1
        degrees[p1] -= 1

    result = []

    dq = deque()
    for i in range(1, N+1):
        if degrees[i] == 0:
            dq.append(i)

    while dq:
        curr = dq.popleft()
        result.append(curr)
        for next in nodes[curr]:
            degrees[next] -= 1
            if degrees[next] == 0:
                dq.append(next)

    if len(result) == N:
        print(" ".join(map(str, result)))
    else:
        print("IMPOSSIBLE")

