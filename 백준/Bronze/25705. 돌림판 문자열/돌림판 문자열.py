import sys
input = sys.stdin.readline

n, s, m, t = int(input()), input().strip(), int(input()), input().strip()
result, curr, cnt = 0, 0, 0

while cnt < m:
    buf = 0
    while s[curr] != t[cnt]:
        buf += 1
        curr = (curr + 1) % n
        if buf >= n*2:
            print(-1)
            exit()
    cnt += 1
    curr = (curr + 1) % n
    result += buf + 1

print(result)
