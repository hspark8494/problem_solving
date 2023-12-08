def solution(myStr):
    return myStr.translate(str.maketrans("abc","   ")).split() or ["EMPTY"]