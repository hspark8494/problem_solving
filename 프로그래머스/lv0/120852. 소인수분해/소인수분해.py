def solution(n):
    li = []
    i = 2;
    while n>1:
        if n%i==0:
            li.append(i)
            n = n//i
            i = 2
        else:
            i+=1
    return sorted(list(set(li)))