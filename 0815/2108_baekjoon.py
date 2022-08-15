import sys

n = int(sys.stdin.readline())
num_list = []

for _ in range(n):
   num_list.append(int(sys.stdin.readline()))

num_list.sort()


# 산술평균
sum_num_list = int(sum(num_list))
if sum_num_list < 0:
    average = int(sum_num_list / n - 0.5)

else:
    average = int(sum_num_list/n + 0.5)

print(average)

# 중앙값 구하기
print(num_list[int(n/2)])

# 최빈값 구하기
a = len(num_list)
count_list = [0] * a
for i in range(1, a):
    if num_list[i] == num_list[i-1]:
        count_list[i] = count_list[i-1] + 1

max_index = max(count_list)
max_idx = 0
cnt = 0
if count_list.count(max_index) > 1:
    for j in range(0, a):
        if count_list[j] == max_index:
            cnt += 1
        if cnt == 2:
            max_idx = j
    print(num_list[max_idx])
else:
    for i in range(a):
        if count_list[i] == max_index:
            max_idx = i
    print(num_list[max_idx])


# 범위 구하기
print(num_list[-1]-num_list[0])

