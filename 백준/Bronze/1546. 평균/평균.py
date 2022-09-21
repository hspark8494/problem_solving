k =int(input())
l = list(map(int, input().split()))
mx = 1
sum = 0

for i in l:
    if i>mx:
        mx=i

for i in range(k):
    l[i] = l[i]/mx*100
    sum = sum+l[i]

print(sum/k)