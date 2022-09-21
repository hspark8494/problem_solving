X = int(input())
S = list(map(int, input().split(" ")))
curr = 0
for next in S:
    curr ^= next

print("koosaga" if curr else "cubelover")