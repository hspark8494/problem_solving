N = input()
F = int(input())
S = int(N[:-2]+'00')%F
print(f"{(F-S)%F:02d}")