N, K = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
acc = 0
for i in range(K):
    acc += nums[i]
mx = acc

for i in range(K, N):
    acc = acc - nums[i-K] + nums[i]
    mx = max(mx, acc)

print(mx)