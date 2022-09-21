i = int(input())
m5 = i//300
i = i%300
m1 = i//60
i = i%60
s = i//10

if i%10 ==0:
    print(m5, m1, s)
else:
    print(-1)