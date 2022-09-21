tmp = [[10], [1], [6,2,4,8], [1,3,9,7], [6,4], [5], [6], [1,7,9,3], [6,8,4,2], [1,9]]
for x in range(int(input())):
    a,b = map(int, input().split())
    a=a%10
    print(tmp[a][b % len(tmp[a])] if a!=0 else 10)