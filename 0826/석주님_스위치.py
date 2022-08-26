# n = int(input())
# switch = [0] * (n+1)
# arr = list(map(int, input().split()))
# for i in range(1, n+1):
#     switch[i] = arr[i-1]
# students = int(input())
# man = list(map(int, input().split()))
# woman = list(map(int, input().split()))
#
# for i in range(1, len(man)):
#     a = man[i]
#     for j in range(a,n+1,a):
#         if switch[j] == 0:
#             switch[j] = 1
#         else:
#             switch[j] = 0
#
# for i in range(1, len(woman)):
#     b = woman[i]
#     k = 0
#     if switch[b] == 1:
#         switch[b] = 0
#     else:
#         switch[b] = 1
#     while True:
#         k += 1
#         print(k)
#         if 1 <= b-k <= n and 1 <= b+k <= n and switch[b-k] == switch[b+k]:
#             if switch[b-k] == 0:
#                 switch[b-k] = 1
#             else:
#                 switch[b-k] = 0
#             if switch[b+k] == 1:
#                 switch[b+k] = 0
#             else:
#                 switch[b+k] = 1
#         else:
#             break

switch=[1,2,3,4,5,6,77,8,9,24,2,3,4,5,6,7,8,3,2,1,6,7,1,2,2,4,5,6,7,8,1]
n = len(switch)

result = ""
for i in range(1,101):
    if i == n + 1:
        break
    result += str(switch[i]) + " "
    if i == 20 or i == 40 or i == 60 or i == 80:
        result += "\n"

print(result)

