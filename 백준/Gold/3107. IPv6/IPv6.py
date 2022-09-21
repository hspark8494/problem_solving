ip = input().split(":")

result = []

flag = False
for i, s in enumerate(ip):
    if s or flag:
        result.append(s.zfill(4))
    else:
        for _ in range(9 - len(ip)):
            result.append("0000")
        flag=True

print(":".join(result))