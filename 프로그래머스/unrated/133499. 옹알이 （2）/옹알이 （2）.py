def solution(babbling):
    s = set(["aya", "ye", "woo", "ma"])
    r = 0
    for babbb in babbling:
        curr, pre = "", ""
        for b in babbb:
            curr += b
            if curr in s and curr != pre:
                pre = curr
                curr = ""
        if curr == "":
            r += 1

    return r
