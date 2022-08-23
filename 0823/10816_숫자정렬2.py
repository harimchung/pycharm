import sys

n = int(sys.stdin.readline().rstrip())
number = list(sys.stdin.readline.split())
print(number)

m = int(sys.stdin.readline().rstrip())
find = list(sys.stdin.readline.split())
count = [0]*m

for i in range(m):
    count[i] += number.count(find[i])

for k in range(m):
    print(count[k], end= " ")
print()
