def b_search(start, end, li, val):
    if start>end:
        return 0
    mid = (start+end) // 2
    if val == li[mid]:
        return 1
    elif val < li[mid]:
        return b_search(start, mid-1, li, val)
    else:
        return b_search(mid+1, end, li, val)

N = int(input())
cards = sorted(list(map(int, input().split(" "))))
M = int(input())
nums = list(map(int, input().split(" ")))
for i in nums:
    print(b_search(0, N-1, cards, i), end=" ")

