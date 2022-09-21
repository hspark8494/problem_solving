a, b = 0, 0
input()
for i in input():
    if i=="A":
        a=a+1
    else:
        b=b+1
print("Tie" if a==b else ("A" if a>b else "B"))