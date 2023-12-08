def solution(numbers, direction):
    if direction == "right":
        t = numbers.pop()
        return [t] + numbers
    else:
        return numbers[1:] + numbers[:1]