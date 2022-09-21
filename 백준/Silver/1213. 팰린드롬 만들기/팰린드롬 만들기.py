import sys
s = list(input())
l = [0]*26
f = (len(s)%2==0)
t = ""

for i in s:
    l[ord(i)-65] += 1

for i in range(26):
    if l[i]%2==1:
        if f or t:
            print("I'm Sorry Hansoo")
            sys.exit()
        else:
            t=chr(i+65)
            l[i]=(l[i]-1)//2
    else:
        l[i]=l[i]//2

r=""
for i in range(26):
    r=r+(chr(i+65)*l[i])
print(r+t+r[::-1])