import sys

x = int(sys.stdin.readline())
s = set()
for line in sys.stdin.readlines():
    E, O = line.strip().split(" ")
    if O == "enter":
        s.add(E)
    elif O == 'leave' and E in s:
        s.remove(E)

print(*sorted(list(s), reverse=True), sep="\n")
