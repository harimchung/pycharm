T = int(input())
for tc in range(1, T+1):

    # n, m은 각각 화덕의 크기와 피자의 개수를 의미한다.
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    visited = [0]*m

    # 먼저 화덕의 크기만큼 들어갈 수 있는 큐를 만든다.
    q = []

    # 초기에 화덕에 들어갈 수 있을 만큼 피자의 치즈와 인덱스를 함께 넣는다.
    for i in range(n):
        q.append([c[i],i])
        visited[i] = 1


    while True:

        # q의 길이가 1이 될 때까지 반복한다.
        if len(q) == 1:
            break
        a = q.pop(0)

        # 만약 치즈의 양이 0이된다면, 다음으로 오븐에 넣을 수 있는 피자를 찾아서 넣는다.
        if a[0] == 0:
            for j in range(m):
                if visited[j] == 0:
                    q.insert(0, [c[j], j])
                    visited[j] = 1
                    break

        # 0이 아니라면, 치즈의 값을 2로 나눈 피자를 다시 넣는다.
        else:
            a[0] = a[0] // 2
            q.append(a)


    print(f"#{tc}", end=" ")
    print(q[0][1] + 1)
