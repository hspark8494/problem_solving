import sys
input = sys.stdin.readline
N, M = map(int, input().split(" "))
li = [0] + list(map(int, input().split(" ")))
acc = 0
for (i,val) in enumerate(li):
    acc += val
    li[i] = acc

for _ in range(M):
    start, end = map(int, input().split(" "))
    print(li[end] - li[start-1])