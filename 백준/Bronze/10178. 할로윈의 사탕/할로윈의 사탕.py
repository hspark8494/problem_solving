for i in range(int(input())):
    n,m = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)."%(n//m,n%m))