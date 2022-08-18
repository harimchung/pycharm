T = int(input())
for tc in range(1, T + 1):
    row = input()

    size = 1000
    top = -1  # top은 가장 위에 있는 인덱스 번호를 의미한다.
    stack = [0] * size

    top += 1
    stack[top] = row[0]  # 제일 처음 글자는 앞 글자가 없으니까 그냥 넣어버리기

    for i in range(1, len(row)):
        if top != -1 and stack[top] == row[i]:  # 스택이 비어있지 않고, 글자가 동일한 경우
            top -= 1
        else:  # 글자가 다르면, push 한다.
            top += 1
            stack[top] += row[i]

    print(f"#{tc} {top + 1}")