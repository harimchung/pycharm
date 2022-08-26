import sys

T = int(sys.stdin.readline())
for tc in range(T):
    # n은 문서의 개수, m번째는 궁금한 수이다.
    n, m = map(int, sys.stdin.readline().split())
    printing = list(map(int, sys.stdin.readline().split()))
    q = [[printing[i], i] for i in range (n)]

    # 입력 예시
    # 4 2 (n = 4, m = 2)
    # 1 2 3 4 (q=[[1,0], [2,1], [3,2], [4,3]])

    done = []

    while True:
        # done 리스트에 타겟이 들어가면 멈춘다.
        if m in done:
            break

        prior = max(printing)
        a = q.pop(0)
        # 현재 우선순위의 차례라면, done에 집어넣는다.
        if a[0] == prior:
            done.append(a[1])
            printing.remove(prior)

        # 현재 우선순위보다 아래라면, 다시 큐에 넣는다.
        else:
            q.append(a)

    print(len(done))
