import math
import itertools
for _ in range(int(input())):
    li = list(map(int, input().split()))
    mx = 1
    for i in itertools.permutations(li, 2):
        mx = max(mx, math.gcd(*i))
    print(mx)
