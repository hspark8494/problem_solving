X, N = map(lambda x : int(x)*1000, input().split(" "))
li = [0, N*7, N+N*2+(N*0.5), N+(N*0.5)+(N*0.25)]
li.sort(reverse=True)
for i in li:
    if X>=i:
        print(int(i))
        break