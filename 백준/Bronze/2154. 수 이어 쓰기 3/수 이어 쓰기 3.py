n = input()
s = "".join(map(str, range(1, int(n)+1)))
print(s.find(n) + 1)