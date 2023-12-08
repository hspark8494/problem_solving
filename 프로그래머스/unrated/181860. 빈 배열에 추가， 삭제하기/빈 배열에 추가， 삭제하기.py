def solution(arr, flag):
    x = []
    for i in range(len(flag)):
        if flag[i]:
            x.extend([arr[i]] * arr[i] * 2)
        else:
            for i in range(arr[i]):
                x.pop()
    return x