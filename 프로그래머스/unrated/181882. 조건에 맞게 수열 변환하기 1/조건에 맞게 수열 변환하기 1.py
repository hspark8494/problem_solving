def solution(arr):
    return list(map(conv, arr))

def conv(t):
    if t>=50 and t%2==0:
        return t//2
    elif t<50 and t%2!=0:
        return t*2
    else:
        return t