import sys

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for _ in range(n)]

for j in range(n-1, -1, -1):
    for i in range(j, n-1):
        if number[i] > number[i+1]:
            number[i], number[i+1] = number[i+1], number[i]

for k in range(n):
    print(number[k])