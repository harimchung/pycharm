n = int(input())
word_list = []
for _ in range(n):
    word = input()
    word_list.append(word)

word_list.sort()

for i in word_list:
    print(i)