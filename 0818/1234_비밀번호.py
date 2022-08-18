# 총 10번에 걸쳐서 출력
for tc in range(1, 11):
    a, b = input().split()
    stack = []

    for char in b:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        elif stack[-1] != char :
            stack.append(char)
    s = ""
    for ss in stack:
        s += ss
    print(f"#{tc} {s}")
