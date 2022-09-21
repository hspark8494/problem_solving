s = input()
while True:
    if len(s)>9:
        print(s[:10])
        s = s[10:]
    else:
        print(s)
        break
