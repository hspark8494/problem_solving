a, b, c = map(int, input().split(" "))
x = a+b
r = 0
while x >= c:
    r += x//c
    x = x//c + x % c
print(r)