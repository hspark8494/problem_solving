s_input = input()
s = set()
for i in range(len(s_input)):
    for j in range(len(s_input)):
        s.add(s_input[i:j+1])

print(len(s)-1)