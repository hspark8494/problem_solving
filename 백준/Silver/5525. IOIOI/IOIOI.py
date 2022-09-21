n = int(input())
input()
s = input()
p = "IOI" + "OI"*(n-1)
l = len(p)
result = 0

for start in range(0, len(s)-l+1):
    if p == s[start:start+l]:
        result+=1

print(result)