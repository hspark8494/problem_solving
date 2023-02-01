N = input()
pre, acc, r = 0, 0, 0
for i in map(int, input().split(" ")):
    if pre > i:
        acc += 1
    else:
        r = max(r, acc)
        acc = 0
        pre = i
print(max(r, acc))