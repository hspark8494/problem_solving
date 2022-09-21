N = int(input())
nums = list(map(int, input().split(" ")))
stack = []
result = [-1 for _ in range(N)]
for x in enumerate(nums):
    if not stack or stack[-1][1] >= x[1]:
        stack.append(x)
    else:
        while stack and stack[-1][1] < x[1]:
            c = stack.pop()
            result[c[0]] = x[1]
        stack.append(x)

print(*result)