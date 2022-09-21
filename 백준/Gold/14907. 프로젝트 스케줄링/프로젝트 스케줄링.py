import heapq, sys

nodes = [[] for _ in range(26)]
degrees = [0] * 26
values = [-1] * 26 
parse = lambda x : ord(x) - 65

lines = sys.stdin.readlines()

for line in lines:
    l = line.rstrip().split(" ")
    curr = parse(l[0])
    values[curr] = int(l[1])
    if len(l) >= 3:
        parents = list(l[2])
        for p in parents:
            x = parse(p)
            degrees[curr] += 1
            nodes[x].append(curr)

pq = []

for i in range(26):
    if degrees[i] == 0 and values[i] >= 0:
        heapq.heappush(pq, (values[i], i))
result = 0

while pq:
    val, curr = heapq.heappop(pq)
    result = max(result, val)
    for next in nodes[curr]:
        degrees[next] -= 1
        if degrees[next] == 0:
            heapq.heappush(pq, (val+values[next], next))
            values[next] = -1

print(result)
