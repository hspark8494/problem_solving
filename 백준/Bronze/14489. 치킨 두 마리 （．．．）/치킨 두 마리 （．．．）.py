n, m = map(int, input().split(" "))
k = int(input())
curr = n+m-(k*2)
if curr >= 0:
    print(curr)
else:
    print(n+m)