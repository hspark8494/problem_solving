from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
nums = defaultdict(int)

for _ in range(N):
    x = 1
    S = input().rstrip()
    for s in reversed(S):
        nums[s] += x
        x = x*10

result = 0
for i, val in enumerate(sorted(nums.values(), reverse=True)):
    result += (9-i) * val

print(result)