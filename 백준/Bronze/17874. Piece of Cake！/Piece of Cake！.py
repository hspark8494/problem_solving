n,w,h = map(int,input().split())
t = max(w,n-w)*max(h,n-h)
print(t*4)