import sys, math
input = sys.stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
li = []
nums.sort()

for i in range(1,N):
    li.append(nums[i]-nums[i-1])

gcd = math.gcd(*li)
result = set()
for i in range(2, int(math.sqrt(gcd))+1):
    if gcd%i == 0:
        result.add(i)
        result.add(gcd//i)
result.add(gcd)
print(*sorted(result))