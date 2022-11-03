N, X = map(int, input().split(" "))
A = list(map(int, input().split(" ")))

i = 0
while True:
    if A[i]<X:
        print(i+1)
        break
    X+=1
    i=(i+1)%N