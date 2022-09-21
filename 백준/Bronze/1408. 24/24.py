s = list(map(int, input().split(":")))
e = list(map(int, input().split(":")))
if s[0]>e[0]:
    e[0]=e[0]+24
k = abs((e[0]*3600+e[1]*60+e[2]) - (s[0]*3600+s[1]*60+s[2]))
print("{0:02d}:{1:02d}:{2:02d}".format(k//3600, k//60%60, k%60))
