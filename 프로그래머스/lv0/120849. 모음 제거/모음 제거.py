chars = ['a','e','i','o','u']
def solution(my_string):
    return "".join(map(lambda x: "" if x in chars else x, my_string))