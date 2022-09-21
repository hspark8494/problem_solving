input()
li = list(input().split())
li.sort(key=lambda x: x*9, reverse=True)
print(int("".join(li)))