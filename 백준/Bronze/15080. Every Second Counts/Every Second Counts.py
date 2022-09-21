T1 = list(map(int, input().split(":")))
T2 = list(map(int, input().split(":")))

t1 = T1[0]*60*60 + T1[1]*60 + T1[2]
t2 = T2[0]*60*60 + T2[1]*60 + T2[2]

if t1 > t2:
    print(86400-t1+t2)
else:
    print(t2-t1)