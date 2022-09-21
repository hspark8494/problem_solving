N = int(input())
a = 0
b = 1
for _ in range(N):
    a, b = b, a+b
print(a*2+b*2)