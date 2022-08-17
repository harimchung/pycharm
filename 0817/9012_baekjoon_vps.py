T = int(input())
for _ in range (T):
    # input의 괄호 하나하나를 list로 바꿔서 받는다.
    input_vps = [c for c in input()]
    answer_list = []
    answer = "YES"

    # 만약에 여는 괄호'(' 이면 list에 push 한다.
    for i in input_vps:
        if i == '(':
            answer_list.append(i)
        else:
            try:
                answer_list.pop(-1)
            except:
                answer = "NO"

    if len(answer_list) != 0:
        answer = "NO"

    print(answer)