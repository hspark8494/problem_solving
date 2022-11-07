G, P, T = map(int, input().split(" "))
K = G + (T*P)
if G*P>K :
    print(2)
elif K>G*P :
    print(1)
else:
    print(0)