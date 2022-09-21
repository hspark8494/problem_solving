h,m,s = map(int, input().split())
d = h*60*60 + m*60 + s + int(int(input()))
print("%d %d %d" % (d/60/60%24, d/60%60, d%60))