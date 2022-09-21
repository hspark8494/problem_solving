l = [0, 0, 0, 0, 0]
for m in range(int(input())):
    i,j = map(int, input().split())

    if i==0 or j == 0:
        l[4] += 1
    elif i>0 and j>0:
        l[0] += 1
    elif i<0 and j>0:
        l[1] += 1
    elif i<0 and j<0:
        l[2] += 1
    else:
        l[3] += 1

for i in range(1,5):
    print("Q%d: %d"%(i, l[i-1]))
print("AXIS: %d"%l[4])