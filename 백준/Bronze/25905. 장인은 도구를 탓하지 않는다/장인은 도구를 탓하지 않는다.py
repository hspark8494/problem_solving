import sys
nums = list(map(float, sys.stdin.readlines()))
curr = 1.0
nums.sort(reverse=True)
for i in range(9):
    curr *= nums[i] / (i+1)

print(curr*10**9)