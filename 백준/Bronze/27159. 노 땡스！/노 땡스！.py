input()
l = sorted(list(map(int, input().split(" "))))
result = 0
pre = -1
for i in l:
    if pre != i - 1:
        result += i
    pre = i

print(result)
