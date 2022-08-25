T = int(input())
for tc in range(1, T+1):

    # n, m은 각각 화덕의 크기와 피자의 개수를 의미한다.
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    oven = [[] for _ in range(n)] # 오븐 안에 화덕의 크기

    next_i = 0 # 다음에 넣을 피자 번호
    for i in range(n):
        oven[i] = [i, pizza.pop(0)]
        next_i += 1

    remain = n # 오븐에 남아있는 피자의 개수
    last_index = -1 # 마지막에 꺼낸 피자의 번호

    # 치즈가 다 녹을 때까지 반복
    while True:
        # 피자번호, 피자를 꺼내기
        i, cheese = oven.pop(0) # i는 피자의 번호, pizza는 치즈

        # 치즈 녹이기
        cheese //= 2

        # 치즈가 다 녹지 않았으면 다시 넣기
        if cheese != 0:
            oven.append([i, cheese])

        # 피자가 다 구워졋다
        else:
            # 더 구울 피자가 남아있다면
            if pizza:
                oven.append([next_i, pizza.pop(0)])
                next_i += 1

            # 더이상 구울 피자가 없다면
            else:
                # 오븐에 남아있는 피자 개수를 감소시킨다.
                remain -= 1

                # 더이상 남아있는 피자의 개수가 없다면
                if remain == 0:
                    # 현재의 피자번호 i가 마지막에 나온 피자의 번호가 된다.
                    last_index = i
                    break

    print(f"#{tc} {last_index+1}")



