a,b,c = map(int, input().split())
print("%d" % max(a*b/c, a/b*c))