import sys
d = {"P":[0]*13,"K":[0]*13,"H":[0]*13,"T":[0]*13}
s = input()

for i in range(0,len(s),3):
    a = s[i]
    t = s[i+1]+s[i+2]
    if t[0]=="0":
        d[a][int(t[1])-1]+=1
    else:
        d[a][int(t[0]+t[1])-1]+=1

r=""
for k,v in d.items():
    for j in v:
        if j>=2:
            print("GRESKA")
            sys.exit()
    r=r+str(13-sum(v))+" "
print(r)