def solution(spell, dic):
    s = set(spell)
    return 1 if len(list(filter(lambda word: len(s) == len(word) and s==set(word), dic))) > 0 else 2