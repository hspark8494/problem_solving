for p in range(int(input())):
    i = int(input())
    s = input()
    s = s.replace("I","1").replace("O","0")
    r = ""
    for x in range(0,i*8,8):
        r=r+chr(int(s[x:x+8],2))
    print("Case #%d: %s" %(p+1,r))