# Q12981 영어 끝말잇기
# https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3
def solution(n, words:list):
    s = set()
    pre = words[0][0]

    for (i, word) in enumerate(words):
        if pre is not word[0] or word in s:
            return [(i%n)+1, (i//n)+1]
        else:
            pre = word[-1]
            s.add(word)

    return [0, 0]