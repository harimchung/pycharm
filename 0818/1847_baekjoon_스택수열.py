import sys

# 먼저 n이라는 변수로 총 길이가 될 숫자 하나를 입력받는다.
n = int(sys.stdin.readline())

# 현재 top 값은 1이다.
top = 1

# 빈 stack1을 생성한다. 여기에는 나중에 빠질 숫자가 담길 곳이다.
stack1 = []
# 답안을 담을 answer 리스트를 생성한다.
answer = []

# 방문했는지의 여부를 담을 list를 만든다.
visited = [0] * (n+1)

# 다음 줄부터 총 길이만큼 숫자를 입력받는다.
for _ in range(n):
    i = int(sys.stdin.readline())
    # i값이 현재 top값보다 같거나 크다면, top값부터 입력받은 숫자까지 더한다.
    if i >= top:
        # 단, stack에 남아있는 숫자만 더한다
        for j in range(top, i+1):
            if visited[j] == 0:
                # push(+)를 answer에 추가하고, 값을 빈 stack1에 추가한다.
                answer.append('+')
                stack1.append(j)
                # visited에는 방문했다고 표시한다.
                visited[j] = 1
        # pop(-)을 answer에 추가 하고, 값을 stack1에서 빼낸다.
        answer.append('-')
        stack1.pop()
        # stack1에 남아있는 값이 있다면,
        if stack1:
            # 현재 top 값은 stack[-1]이다.
            top = stack1[-1]
    # 현재 top 값보다 작다면,
    else :
        # stack1에서의 top 값이 i와 같은지 비교한다.
        if top == i:
            # 맞고, 뺄 수 있는 요소가 stack1에 남아있다면
            if stack1:
                # anwer에 pop(-)을 더한다.
                answer.append('-')
                # top값을 뽑아내고
                stack1.pop()
                # stack1 값에 남는 값이 있다면 top 값을 갱신한다.
                # 다시 반복문을 돌린다.
                if stack1:
                    top = stack1[-1]

        else :
            # top값이 들어온 i 값이 아니라면, answer 리스트를 초기화(clear)하고,
            answer.clear()
            # NO를 담고 반복문을 탈출한다.
            answer.append("NO")
            break

# 반복문이 끝난다음에
# answer리스트 안에 있는 요소들에 대해서 한줄씩 출력한다.
print = sys.stdout.write
for ans in answer:
    print(ans+'\n')