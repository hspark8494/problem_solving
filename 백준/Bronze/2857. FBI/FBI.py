import sys
li = []
for (i, line) in enumerate(sys.stdin.readlines()):
    if line.find("FBI") > -1:
        li.append(i+1)
    
if li:
    print(*li)
else:
    print("HE GOT AWAY!")