li ="aeiouAEIOU"
for i in range(int(input())):
    s = input().replace(" ","")
    c = 0
    for d in s:
        m = li.find(d)
        if m>=0:
            c=c+1
    print(len(s)-c, c)