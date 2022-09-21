import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    S, D = map(int, input().rstrip().split(" "))

    result = 0
    for i in range(S):
        speed, fuel, e = map(int, input().rstrip().split(" "))
        if D/speed <= fuel/e:
            result+=1

    print(result)