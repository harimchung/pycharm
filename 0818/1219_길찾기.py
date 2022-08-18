import sys
sys.stdin = open('길찾기.txt')

for _ in range(10):
    # 길이가 100인 배열 2개를 만든다. (빈 곳은 -1로 채운다.)
    list1 = [-1]*100
    list2 = [-1]*100
    # a는 테스트케이스넘버, b는 간선의 숫자를 의미한다.
    tc, b = map(int, input().split())
    adjs = input().split()
    n = len(adjs)
        # 입력받은 문자열에 대해서
        # 0, 2, 4 ... 2n번의 수는 인덱스를
        # 1, 3, 5 ... 홀수번째 수는 들어갈 수를 의미한다.

    for i in range(0, n-1, 2):
        # 첫번째 테스트케이스에서
        # a = 0, 0, 1, 1, ...
        a = int(adjs[i])
        # 1번 리스트가 비었다면 먼저 1번 리스트에 넣어본다.
        if list1[a] == -1:
            list1[a] = int(adjs[i+1])
        # 1번 리스트에 이미 있다면 2번 리스트에 넣는다.
        else :
            list2[a] = int(adjs[i+1])


    # dfs를 이용해서 0에서 출발해서 99까지 도달할 수 있는지 구한다.
    # 지금 준비된 것은 인접한 숫자리스트이다.
    # 여기에서는 현재위치가 99가 되면 무조건 break 하는 것이 특징이다.
    # 마지막으로 방문한 곳을 담을 stack 을 만든다.
    # ans = 1 , 즉 일단 도달할 수 있다고 가정한다.

    stack = []
    now = 0

    while True:
        ans = 1
        # 만약 현재위치가 99가 된다면 무조건 break.
        # 현재 출발 위치(now) = 0
        if now == 99:
            break
        # list1을 우선적으로 순회한다.
        # list1[현재위치] != -1이 아니라면
        if list1[now] != -1:
            # stack에 now를 추가하고
            stack.append(now)
            # now = list1의 현재인덱스의 값으로 이동한다.
            now = list1[now]

        # list1[현재위치] == -1 이면, 더이상 갈 곳이 없다는 뜻이다.
        else :
            top = stack.pop()
            # 만약 list2의 스택의 마지막 값 != -1이라면 갈 곳이 있으므로,
            if list2[top] != -1:
                # 다시 이동해본다.
                now = list2[top]
            # 마지막 값이 -1 이라면, 더이상 이동할 수 없으므로,
            else:
                # ans = 0으로 바꾸고 반복문을 중단한다.
                ans = 0
                break
    print(f"#{tc} {ans}")

