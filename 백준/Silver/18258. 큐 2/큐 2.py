import collections
import sys
deq = collections.deque()

for _ in range(int(sys.stdin.readline())):
    o = sys.stdin.readline().split()
    try:
        if o[0] == "push":
            deq.appendleft(int(o[1]))
        elif o[0] == "push_back":
            deq.append(int(o[1]))
        elif o[0] == "pop_front":
            print(deq.popleft())
        elif o[0] == "pop":
            print(deq.pop())
        elif o[0] == "size":
            print(len(deq))
        elif o[0] == "empty":
            print(1 if len(deq)==0 else 0)
        elif o[0] == "front":
            print(deq[-1])
        elif o[0] == "back":
            print(deq[0])
    except:
        print(-1)