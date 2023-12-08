def solution(arr, idx):
    try:
        return arr.index(1, idx)
    except:
        return -1