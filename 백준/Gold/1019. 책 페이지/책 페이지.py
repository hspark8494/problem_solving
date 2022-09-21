n = int(input())
s = [0 for i in range(10)]
p = 1

while n != 0:
    while n % 10 != 9:
        for i in str(n):
            s[int(i)] += p
        n -= 1
    if n < 10:
        for i in range(n + 1):
            s[i] += p
        s[0] -= p
        break
    else:
        for i in range(10):
            s[i] += (n // 10 + 1) * p

    s[0] -= p
    p *= 10
    n //= 10

print(*s)
