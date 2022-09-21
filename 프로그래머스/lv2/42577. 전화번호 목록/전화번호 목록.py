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