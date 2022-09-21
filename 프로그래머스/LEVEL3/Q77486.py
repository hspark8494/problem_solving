# Q77486 다단계 칫솔 판매
# https://school.programmers.co.kr/learn/courses/30/lessons/77486
import math

class tree:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.childern = []
        self.sales = 0

def solution(enroll, referral, seller, amount):
    users = {}
    root = tree("center")
    for name in enroll:
        users[name] = tree(name)
    for (i, name) in enumerate(referral):
        t = root
        if name != "-":
            t = users[name]
        users[enroll[i]].parent = t
        t.childern.append(users[enroll[i]])

    for i in range(len(seller)):
        curr = users[seller[i]]
        price = amount[i] * 100
        while curr.parent != None and price>0:
            curr.sales += (price - price//10)
            price = (price // 10)
            curr = curr.parent
        curr.sales += price

    answer = []

    for name in enroll:
        answer.append(math.ceil(users[name].sales))
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],  ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))