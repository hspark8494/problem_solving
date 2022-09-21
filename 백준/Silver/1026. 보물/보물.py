int(input())
li1 = list(map(int, input().split(" ")))
li2 = list(map(int, input().split(" ")))
li1.sort()
li2.sort(reverse=True)
result=0
for i in range(len(li1)):
	result += li1[i]*li2[i]
print(result)
