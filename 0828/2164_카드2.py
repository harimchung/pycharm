import sys
from collections import deque
n = int(sys.stdin.readline())

q = [i for i in range(1, n+1)]
q = deque(q)

while q:
    if len(q) == 1:
        break
    q.popleft()
    a = q.popleft()
    q.append(a)


b = q.popleft()
print(b)
