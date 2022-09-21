import sys, math
input = sys.stdin.readline

S = int(input())
for _ in range(S):
    N = int(input())
    nums = list(map(int, input().rstrip().split(" ")))

    li = []
    nums.sort()

    for i in range(1,N):
        li.append(nums[i]-nums[i-1])

    result = math.gcd(*li)
    print(result if result else "INFINITY")
