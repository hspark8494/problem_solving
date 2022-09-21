from sys import stdin
input = stdin.readline
s = set()
for _ in range(int(input().rstrip())):
    l = input().rstrip().split(" ")
    op = l[0]
    val = 0
    if len(l) >= 2:
        val = int(l[1])
    try:
        if op == "add":
            s.add(val)
        elif op == "check":
            print(int(val in s))
        elif op == "remove":
            s.remove(val)
        elif op == "toggle":
            if val in s:
                s.remove(val)
            else:
                s.add(val)
        elif op == "all":
            s = set(range(1, 21))
        elif op == "empty":
            s.clear()
    except:
        pass
