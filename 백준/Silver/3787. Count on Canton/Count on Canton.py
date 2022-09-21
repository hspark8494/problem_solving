import sys

lines = sys.stdin.readlines()

for line in lines:
    n = int(line.rstrip())
    l = 0
    end = 0

    while n > end:
        l += 1
        end += l

    k = end - n
    if l%2 == 0:
        top = l - k
        bot = k + 1
    else:
        top = k + 1
        bot = l - k

    print(f"TERM {n} IS {top}/{bot}")