from math import sqrt

x = 0
for c in list(input().rstrip()):
    if c>"Z":
        x += ord(c) - 96
    else:
        x += ord(c) - 38
isprime = True
for i in range(2, int(sqrt(x))+1):
    if x%i==0:
        isprime=False
        break

if x<=2 or isprime:
    print("It is a prime word.")
else:
    print("It is not a prime word.")