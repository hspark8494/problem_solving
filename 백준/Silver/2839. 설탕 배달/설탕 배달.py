n = int(input())
x3 = 0
x5=int(n/5)
x3=int((n-(x5*5))/3)
bol = False
for i in range(x5+1):
    if x5 * 5 + x3 * 3 != n:
        x5=x5-1
        x3=int((n-(x5*5))/3)
    else:
        bol=True
        break
print(x5+x3 if bol else -1)