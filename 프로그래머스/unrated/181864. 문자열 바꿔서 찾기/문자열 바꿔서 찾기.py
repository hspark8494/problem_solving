def solution(myString, pat):
    return int(pat in "".join(map(lambda x: "A" if x=="B" else "B", myString)))