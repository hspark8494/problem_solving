import sys
for i in range(3):
    
    l = [int(sys.stdin.readline()) for j in range(int(sys.stdin.readline()))]
    d = sum(l)
    print("+" if d>0 else (d if d==0 else "-"))