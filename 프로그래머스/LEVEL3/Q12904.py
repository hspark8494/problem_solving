# Q12904 가장 긴 팰린드롬
# https://school.programmers.co.kr/learn/courses/30/lessons/12904
def solution(s):
    s = "#"+"#".join(list(s))+"#"
    a = [0] * len(s)
    p = 0
    r = 0
    for i in range(len(s)):
        if i<=r:
            a[i] = min(r-i, a[2*p-i])
        else:
            a[i] = 0

        while i-a[i]-1 >= 0 and i + a[i] + 1< len(s) and s[i-a[i]-1] == s[i+a[i]+1]:
            a[i] += 1
            
        if r<i+a[i]:
            r=i+a[i]
            p=i

    return a