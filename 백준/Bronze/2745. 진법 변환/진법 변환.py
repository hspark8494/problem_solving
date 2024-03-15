import sys
input = sys.stdin.readline

S, K = input().rstrip().split(" ")
S = S[::-1]
K = int(K)
X = 0
for k, s in enumerate(S):
    i = int(s) if s.isnumeric() else ord(s) - 55
    X += i * (K ** k)

print(X)