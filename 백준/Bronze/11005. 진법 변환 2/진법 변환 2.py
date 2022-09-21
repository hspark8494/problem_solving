N, B = map(int, input().split(" "))
stack = []

while N>=B:
    stack.append(N%B)
    N = N//B

stack.append(N)
result = ""
while stack:
    curr = stack.pop()
    if curr >= 10:
        result += chr(curr+55)
    else:
        result += str(curr)
print(result)
