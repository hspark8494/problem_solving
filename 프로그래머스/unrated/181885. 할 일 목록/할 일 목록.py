def solution(todo_list, finished):
    t = []
    for i in range(len(todo_list)):
        if not finished[i]:
            t.append(todo_list[i])
    return t