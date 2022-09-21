x = [int(input()) for _ in range(4)]
x.sort()
print(sum(x[1:])+max(int(input()),int(input())))