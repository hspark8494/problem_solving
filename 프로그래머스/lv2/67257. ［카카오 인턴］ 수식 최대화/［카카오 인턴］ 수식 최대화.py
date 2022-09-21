import re

def solution(expression):
    exp = re.findall('([-*+]|[0-9]+)', expression)
    pos = ["+-*", "+*-", "*-+", "*+-", "-*+", "-+*"]
    
    def cacl(a, op, b):
        a = int(a)
        b = int(b)
        if(op == "*"): return a*b
        elif(op == "+"): return a+b
        else: return a-b

    mx = 0
    for x in pos:
        tmp = [*exp]
        for op in x:
            idx = 1
            while(idx<len(tmp)):
                if(tmp[idx] == op):
                    tmp[idx-1] = cacl(tmp[idx-1], tmp[idx], tmp[idx+1])
                    del tmp[idx]
                    del tmp[idx]
                else:
                    idx= idx+2
        mx = max(abs(tmp[0]), mx)
    return mx