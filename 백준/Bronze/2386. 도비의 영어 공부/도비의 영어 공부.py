while True:
    s = input()
    if s == "#":
        break
    s = s.lower()
    print("%s %d" %(s[0], s.count(s[0])-1))