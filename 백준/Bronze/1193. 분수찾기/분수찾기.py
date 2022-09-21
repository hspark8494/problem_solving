n = int(input())
l = 0
end = 0

while n > end:
    l += 1
    end += l

k = end - n
if l%2 == 0:
    top = l - k
    bot = k + 1
else:
    top = k + 1
    bot = l - k

print(f"{top}/{bot}")