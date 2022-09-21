from collections import defaultdict

def solution(survey, choices):
    l = "RTCFJMAN"
    d = defaultdict(int)
    result = ""
    
    for i in range(len(choices)):
        r = 4 - choices[i]
        if r<0:
            d[survey[i][1]] -= r
        else:
            d[survey[i][0]] += r

    for i in range(0, 8, 2):
        if d[l[i+1]] > d[l[i]]:
            result += l[i+1]
        else:
            result += l[i]
            
    return result