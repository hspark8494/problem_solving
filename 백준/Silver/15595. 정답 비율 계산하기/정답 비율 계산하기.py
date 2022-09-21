import sys

d = {}

for i in range(int(input())):
    data = sys.stdin.readline().split(" ")
    if data[1] == "megalusion":
        continue
    if data[1] in d:
        d[data[1]].append(data[2])
    else:
        d[data[1]] = [data[2]]

succeed = 0
failed = 0

for data in d.values():
    tmp = 0
    for i in data:
        if i == "4":
            succeed += 1
            failed+=tmp
            break
        else:
            tmp += 1

print(succeed / (succeed+failed)*100 if succeed != 0 else 0)
