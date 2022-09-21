def reset(li):
    for i in range(len(li)):
        li[i] = False

def test(s):
    brace = 0

    li = [False, False, False, False] # op, closed, opened, numberic
    for i, c in enumerate(s):
        if c.isnumeric():
            if li[1]:
                return False
            reset(li)
            li[3] = True
        elif "*/+-".find(c) > -1:
            if li[0] or li[2] or i==0:
                return False
            reset(li)
            li[0] = True
        elif c =="(":
            brace += 1
            reset(li)
            li[2] = True
        elif c ==")":
            brace -= 1
            reset(li)
            li[1] = True
            if brace < 0:
                return False
        else:
            return False
    return brace == 0 and not li[0] and not li[2]

s = input()
if(test(s)):
    try:
        s = s.replace("/", "//")
        print(format(eval(s), "d"))
    except:
        print("ROCK")
else:
    print("ROCK")