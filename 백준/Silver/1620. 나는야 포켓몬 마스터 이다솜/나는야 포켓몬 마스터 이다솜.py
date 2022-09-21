from sys import stdin
input = stdin.readline

n, q = map(int, input().split(" "))
dic = {}
li = [""]

for i in range(1, n+1):
    name = input().rstrip()
    dic[name] = i
    li.append(name)

for _ in range(q):
    query = input().rstrip()
    try:
        i = int(query)
        print(li[i])
    except:
        print(dic[query])