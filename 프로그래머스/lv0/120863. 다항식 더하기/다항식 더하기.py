def solution(polynomial: str):
    x, i = 0, 0
    for l in polynomial.split(" "):
        if l[-1] == 'x':
            if len(l) == 1:
                x += 1
            else:
                x += int(l[:-1])
        elif l != '+':
            i += int(l)
    l = []
    if x>1:
        l.append(f"{x}x")
    elif x==1:
        l.append("x")
    
    if i>0:
        l.append(str(i))

    return " + ".join(l)



print(solution("x + 1"))