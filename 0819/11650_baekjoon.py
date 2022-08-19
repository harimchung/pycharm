# 좌표 정렬하기
import sys

# 먼저 n이라는 변수로 총 길이가 될 숫자 하나를 입력받는다.
n = int(sys.stdin.readline())
coor = [list() for __ in range(n)]

for i in range (n):
    a, b = map(int, sys.stdin.readline().split())
    coor[i].append(a)
    coor[i].append(b)
print(coor)

# x좌표끼리 비교 후 정렬
# 버블소트... 넘 시간이 오래 걸리려나?
for i in range(n):
    for j in range(i, n):
        if
