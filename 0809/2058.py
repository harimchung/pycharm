# 1. 정수형으로 입력받아서 나머지를 저장하는 방법
n = int(input())
sum = 0
while n > 0:
    sum = sum + n % 10
    n = n//10
print(sum)

# 2. str으로 입력받아서 순회하면서 더하는 방법
numbers = input()
second_sum = 0
for number in numbers:
    second_sum += int(number)
print(second_sum)