T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_dictionary = {}
    # str1에 들어있는 문자들로 딕셔너리를 만든다.
    for i in str1:
        str1_dictionary[i] = 0

    # str2에 str1의 딕셔너리가 나올때마다 +1 시킨다.
    for j in str2:
        if str1_dictionary.get(j) != None:
            str1_dictionary[j] += 1

    # 딕셔너리의 value 값 중에 제일 큰 값을 찾는다.
    max_values = 0
    for value in str1_dictionary.values():
        if value > max_values:
            max_values = value
    # max_values = max(str1_dictionary.values())
    print(f"#{tc} {max_values}")