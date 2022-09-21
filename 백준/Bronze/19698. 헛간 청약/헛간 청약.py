n,w,h,l = map(int,input().split())
r=(w//l) * (h//l)
print(r if r<n else n)