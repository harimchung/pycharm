import sys

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for _ in range(n)]
print(number)

for j in range(0, n-1):
    for i in range(j, n-1):
        if number[i] > number[i+1]:
            number[i], number[i+1] = number[i+1], number[i]

print(number)