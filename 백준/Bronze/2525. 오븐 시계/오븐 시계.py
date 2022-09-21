h, m = map(int,input().split())
c = int(input())
d = h*60+m+c

print(int(d/60%24), d%60)