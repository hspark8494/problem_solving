for _ in range(int(input())):
    n = int(input())
    s=m=0
    for _ in range(n):
        t1,t2 = input().split()
        s=s+int(t1)
        m=m+int(t1)*float(t2)
    print(s, m/s)