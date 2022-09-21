import sys, math
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split(" ")))

li = []
nums.sort()

for i in range(1,N):
    li.append(nums[i]-nums[i-1])

print(math.gcd(*li))