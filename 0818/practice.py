# a = [1,2,3,4,5]
# print(*a)
#
# for i in a:
#     print(i, end=" ")
#
# for j in a:

# a = [1,2,3,4,5,6]
# b = a.pop(-1)
# print(b)
# print(a)
#
# c = input()
# word_list = []
# for word in c:
#     if word == "a":
#         word_list.append(word)
# print(word_list)

adjs = input().split()
print(adjs)

list1 = [-1]*100
list2 = [-1]*100

n = len(adjs)
    # 입력받은 문자열에 대해서
    # 0, 2, 4 ... 2n번의 수는 인덱스를
    # 1, 3, 5 ... 홀수번째 수는 들어갈 수를 의미한다.

for i in range(0, n-1, 2):


    a = int(adjs[i])

    # 1번 리스트가 비었다면 먼저 1번 리스트에 넣어본다.
    if list1[a] == -1:
        list1[a] = adjs[i+1]
    # 1번 리스트에 이미 있다면 2번 리스트에 넣는다.
    else :
        list2[a] = adjs[i+1]
print(list1)
print(list2)