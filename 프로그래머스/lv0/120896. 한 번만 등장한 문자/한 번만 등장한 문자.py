def solution(s):
    chars = [0]*26
    for i in s:
        chars[ord(i)-97]+=1
    result = ""
    for i,c in enumerate(chars):
        if c==1:
            result += chr(i+97)

    return result