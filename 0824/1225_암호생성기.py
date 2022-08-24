for _ in range(10):
    # 테스트케이스의 번호가 입력된다.
    tc = int(input())

    # 숫자 8개가 입력된다.
    nums = list(map(int, input().split()))
    flag = False
    # 한 요소가 0이 될 때까지 사이클을 반복합니다.
    # 시간이 오지게 걸립니다.
    while True:
        # 한 사이클
        for i in range(1,6):
            a = nums.pop(0)
            a = a-i

            if a <= 0:
                nums.append(0)
                flag = True
                break
            nums.append(a)

        if flag:
            break
    print(f"#{tc}", end=" ")
    print(*nums)
