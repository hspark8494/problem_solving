import sys

input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1:
        break
    pre = 0
    result = 0
    for _ in range(N):
        speed, time = map(int, input().split(" "))
        result += speed * (time - pre)
        pre = time
    print(result, "miles")