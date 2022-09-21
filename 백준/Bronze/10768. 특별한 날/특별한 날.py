m = int(input())
d = int(input())
if m==2 and d==18:
    print("Special")
elif m>=3 or (m==2 and d>=19):
    print("After")
else:
    print("Before")