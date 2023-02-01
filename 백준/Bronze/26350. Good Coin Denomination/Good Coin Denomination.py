import sys
input = sys.stdin.readline
x = int(input())
for y in range(x):
    S = list(map(int, input().rstrip().split(" ")))
    pre = S[1]
    f = 'Good coin denominations!'
    for i in range(2, len(S)):
        if S[i] >= pre * 2:
            pre = S[i]
        else:
            f = 'Bad coin denominations!'
            break
    print('Denominations:', *S[1:], sep=" ")
    print(f)
    if x != y+1:
        print()