N = int(input())
seive = [(i % 2 != 0) for i in range(max(3, N+1))]
seive[1] = False
seive[2] = True
primes = [2]
for i in range(3, N+1, 2):
    if seive[i]:
        primes.append(i)
        for j in range(i+i, N+1, i):
            seive[j] = False

result = 0
acc = 0
end = 0
ln = len(primes)
for start in range(ln):
    while (acc < N) and (end < ln):
        acc += primes[end]
        end += 1
    if acc == N:
        result += 1
    acc -= primes[start]

print(result)
