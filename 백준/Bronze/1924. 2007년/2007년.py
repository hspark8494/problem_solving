m = [0,31,28,31,30,31,30,31,31,30,31,30]
d = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
x,y = map(int, input().split())
r = (sum(m[:x])+y)%7
print(d[r])