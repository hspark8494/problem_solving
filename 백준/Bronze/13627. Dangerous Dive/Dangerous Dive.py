S, N = map(int, input().split(" "))
R = set(map(int, input().split(" ")))
if S == N:
    print("*")
else:
    R = set(range(1, S+1)) - R
    print(*sorted(list(R)))