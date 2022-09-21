def oNum(i):
    if i < 100:
        return True
    else:
        s = str(i)
        d = int(s[0]) - int(s[1])

        for k in range(1, len(s)-1):
            if int(s[k]) - int(s[k+1]) != d:
                return False

        return True


n = int(input())
r = 0

for i in range(1,n+1):
    r = r+int(oNum(i))

print(r)