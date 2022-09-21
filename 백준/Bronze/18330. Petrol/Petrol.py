K, N = int(input()), int(input())
R = max(0, K - (N+60))
print((K-R)*1500 + R*3000)