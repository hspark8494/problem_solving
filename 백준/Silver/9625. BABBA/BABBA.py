K = int(input())
a = 0
b = 1
for _ in range(K-1):
    a, b = b, a+b
print(a, b)