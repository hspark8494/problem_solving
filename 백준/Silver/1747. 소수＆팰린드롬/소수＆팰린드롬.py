import math
def isPrime(x) -> bool:
    e = int(math.sqrt(x))
    for i in range(2, e+1):
        if x%i==0 :
            return False
    return True

x = int(input())
if x==1:
    print(2)
else:
    while True:
        s = str(x)
        if s == s[::-1]:
            if isPrime(x):
                print(x)
                break
        x=x+1