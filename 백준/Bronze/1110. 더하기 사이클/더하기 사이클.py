s = input()
n = 0

if int(s)<10:
    s = "0" + s
k = s
while True:
    n=n+1
    t = str(int(s[0])+int(s[1]))
    if int(t)<10:
        t = "0" + t
    s = s[1] + t[1]

    if k==s:
        print(n)
        break