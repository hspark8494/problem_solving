N, X = map(int, input().split())
li = list(map(int, input().split()))

curr, mx, cnt = 0, 0, 1
for i in range(N):
    if i < X:
        curr += li[i]
        mx = curr
    else:
        new_val = curr + li[i] - li[i-X]
        if new_val == mx:
            cnt += 1
        elif new_val > mx:
            mx = new_val
            cnt = 1
        curr = new_val

if mx == 0:
    print("SAD")
else:
    print(mx)
    print(cnt)
