m = [0,31,28,31,30,31,30,31,31,30,31,30]
d = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
y,x = map(int, input().split())
r = (sum(m[:x])+y)%7
print(d[r])