memo = [1, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    ln = len(memo)
    for i in range(ln, x+1):
        memo.append(memo[i-2]+memo[i-3])
    print(memo[x])