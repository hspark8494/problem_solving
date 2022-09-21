# Q42577 전화번호 목록
# https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book:list):
    phone_book.sort(key=lambda x: -len(x))
    trie = {}
    for phone_number in phone_book:
        curr = trie
        check = True
        for n in phone_number:
            if n in curr:
                curr = curr[n]
            else:
                curr[n] = {}
                curr = curr[n]
                check = False
        if check: return False
    return True

solution(["123","456","789"])