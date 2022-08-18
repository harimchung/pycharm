# a = [1,2,3,4,5]
# print(*a)
#
# for i in a:
#     print(i, end=" ")
#
# for j in a:

a = [1,2,3,4,5,6]
b = a.pop(-1)
print(b)
print(a)

c = input()
word_list = []
for word in c:
    if word == "a":
        word_list.append(word)
print(word_list)