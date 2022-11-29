alpha = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(numbers):
    r = ""
    s = ""
    for c in numbers:
        s += c
        if s in alpha:
            r += alpha[s]
            s = ""
    return int(r)