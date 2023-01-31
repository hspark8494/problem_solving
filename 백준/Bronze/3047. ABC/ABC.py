nums = sorted(list(map(int, input().split(" "))))
for c in input():
    print(nums[ord(c) - 65], end = " ")