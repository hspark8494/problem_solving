import sys

nums = list(map(int, sys.stdin.readlines()))

if nums[0] == nums[1] == nums[2] == nums[3]:
    print("Fish At Constant Depth")
else:
    pre = nums[0]
    rise = True
    fall = True
    for i in range(1,4):
        if nums[i]>=pre:
            fall = False
        if nums[i]<=pre:
            rise = False
        pre = nums[i]
    if rise:
        print("Fish Rising")
    elif fall:
        print("Fish Diving")
    else:
        print("No Fish")