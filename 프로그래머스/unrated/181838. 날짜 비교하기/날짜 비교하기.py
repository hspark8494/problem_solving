def solution(date1, date2):
    return int((date1[0] < date2[0]) or (date1[0] == date2[0] and date1[1] < date2[1]) or (date1[0] == date2[0] and date1[1] == date2[1] and date1[2] < date2[2]))