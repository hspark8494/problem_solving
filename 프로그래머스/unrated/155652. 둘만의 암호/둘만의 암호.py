def solution(s, skip, index):
    l = ""
    for i in range(26):
        c = chr(ord('a') + i)
        if c not in skip:
            l += c
    l *= 3
    result = ""
    for c in s:
        i = l.find(c)
        result += l[i + index]
    return result