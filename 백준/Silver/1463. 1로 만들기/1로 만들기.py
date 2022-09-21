memo = [0,0,1,1]
n = int(input())
while len(memo)<=n:
    curr = len(memo)
    mn = memo[-1]
    if curr%3==0:
        mn = min(mn, memo[curr//3])
    if curr%2==0:
        mn = min(mn, memo[curr//2])
    memo.append(mn+1)

print(memo[n])