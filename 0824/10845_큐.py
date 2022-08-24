import sys

n = int(sys.stdin.readline().rstrip())
queue = []
for _ in range(n):

    order = sys.stdin.readline().split()
    if order[0] == "push":
        queue.append(order[1])
    if order[0] == "pop":
        if queue:
            a = queue.pop(0)
            print(a)
        else:
            print("-1")
    if order[0] == "size":
        print(len(queue))
    if order[0] == "empty":
        print("0") if queue else print("1")
    if order[0] == "front":
        print(queue[0]) if queue else print("-1")
    if order[0] == "back":
        print(queue[-1]) if queue else print("-1")
