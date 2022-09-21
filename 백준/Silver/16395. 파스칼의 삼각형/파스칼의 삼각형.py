N, K = map(int, input().split(" "))
arr = [[1]]
for i in range(N-1):
    li = [1]
    for j in range(1,len(arr[i])):
        li.append(arr[i][j-1]+arr[i][j])
    li.append(1)
    arr.append(li)
print(arr[N-1][K-1])