from collections import defaultdict

def solution(array):
    d = defaultdict(int)
    for i in array:
        d[i] += 1
    s = sorted(d.items(), key=lambda x: x[1], reverse=True)
    
    return -1 if len(s)>1 and s[0][1]==s[1][1] else s[0][0]
