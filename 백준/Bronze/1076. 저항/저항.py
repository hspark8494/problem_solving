d = {"black":"0", "brown":"1", "red":"2", "orange":"3", "yellow":"4", "green":"5", "blue":"6", "violet":"7", "grey":"8", "white":"9"}
a=d.get(input())
b=d.get(input())
c=10**int(d.get(input()))

print(int(a+b)*c)