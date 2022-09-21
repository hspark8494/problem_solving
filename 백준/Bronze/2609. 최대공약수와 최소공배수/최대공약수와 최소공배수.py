def gcd(x,y):
    r = x%y
    return y if r==0 else gcd(y,r)

a,b = map(int, input().split())
d = gcd(a,b)

print(d, a*b // d, end="\n")