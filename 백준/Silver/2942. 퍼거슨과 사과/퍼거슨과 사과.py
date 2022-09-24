import math

a, b = map(int, input().split(" "))
gcd = math.gcd(a, b)

divisor = set([1, gcd])
for i in range(2,  gcd//2+1):
    if gcd % i == 0:
        divisor.add(i)
        divisor.add(gcd//i)

for i in divisor:
    print(i, a//i, b//i)
