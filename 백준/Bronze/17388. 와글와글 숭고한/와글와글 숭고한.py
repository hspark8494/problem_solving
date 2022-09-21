li = list(map(int, input().split()))
if sum(li) >= 100:
    print("OK")
else:
    s = ["Soongsil", "Korea", "Hanyang"]
    print(s[li.index(min(li))])