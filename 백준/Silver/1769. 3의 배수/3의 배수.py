S = input()
R = 0
while len(S) > 1:
    R += 1
    S = str(sum(map(int, S)))
print(R)
print("YES" if int(S)%3 == 0 else "NO")