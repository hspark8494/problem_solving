d = [1,1,2,2,2,8]
l = list(map(int,input().split()))
print(*(d[i]-l[i]for i in range(6)))