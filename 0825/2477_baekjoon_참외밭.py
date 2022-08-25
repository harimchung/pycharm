import sys

k = int(sys.stdin.readline())

# 다음에 방향을 나타내는 숫자와 각각의 길이가 주어진다.
# ->, <- , 하, 상
nums = [[] for _ in range(5)]
tong = []

# 2~7번째 줄에 걸쳐서 각 변에 대한 크기가 주어진다.
for _ in range(6):
    a, b = map(int, sys.stdin.readline().split())
    nums[a].append(b)

# 1~2 번째 줄에서 길이의 개수가 한개인 것이 가로가 된다.
for i in range(1,3):
    if len(nums[i]) == 1:
        width = nums[i][0]
        break

# 3~4번째 리스트에서 길이의 개수가 한개인 것이 세로가 된다.
for j in range(3,5):
    if len(nums[j]) == 1:
        height = nums[j][0]
        break


