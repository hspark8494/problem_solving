# Q17677 뉴스 클러스터링
# https://school.programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict

def solution(str1, str2):
    dic = defaultdict(lambda: 0)
    r = 0
    jaccard = 0

    for i in range(len(str1)):
        t = str1[i:i+2].lower()
        if not t.isalpha() or len(t) != 2:
            continue
        dic[t] += 1
        r += 1

    for i in range(len(str2)):
        t = str2[i:i+2].lower()
        if not t.isalpha()  or len(t) != 2:
            continue
        if dic[t] >= 1:
            dic[t] -=1
            jaccard += 1
        else:
            r += 1

    return 65536 if r==0 else int((jaccard/r)*65536)
