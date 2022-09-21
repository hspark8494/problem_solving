N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
result = 0
pos = 0
mn = 0
while pos<N-1:
    if cities[mn]>cities[pos]:
        mn=pos
    else:
        result += cities[mn] * roads[pos]
        pos+=1

print(result)