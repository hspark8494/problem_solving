nums = [
    "0000   1222233334  455556666777788889999",
    "0  0   1   2   34  45   6      78  89  9",
    "0  0   122223333444455556666   788889999",
    "0  0   12      3   4   56  6   78  8   9",
    "0000   122223333   455556666   78888   9"]

n = input()
l = []
for s in n:
    i = int(s)
    for line in nums:
        print(line[(i*4):(i*4+4)].rstrip())
    print()
