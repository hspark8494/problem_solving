def solution(words):
    trie = {}
    for word in words:
        curr = trie
        for w in word:
            if w in curr:
                curr = curr[w]
                curr["end"] = None
            else:
                curr[w] = {}
                curr = curr[w]
    result = 0
    for word in words:
        curr = trie
        dept = 0
        for w in word:
            curr = curr[w]
            dept+=1
            if len(curr) <= 1:
                break
        result += dept
    return result