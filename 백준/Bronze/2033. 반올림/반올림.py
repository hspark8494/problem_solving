N = int(input())

radix = 10
while N > radix:
    if N % radix//(radix//10) >= 5:
        N = (N//radix*radix) + radix
    else:
        N = N//radix*radix
    radix *= 10
print(N)
