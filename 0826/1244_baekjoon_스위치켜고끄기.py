import sys

# 남학생인 경우
def boy(m, n, l):
    # l은 현재 상태의 리스트를 의미한다.
    # m은 자신이 부여받은 번호를 의미한다.
    # n은 전체 리스트 길이를 의미한다.
    for i in range(m, n+1, m):
        if l[i] == 0:
            l[i] = 1
        else:
            l[i] = 0
    return l

# 여학생인경우
def girl(m,n,l):
    # l은 현재 상태의 리스트를 의미한다.
    # m은 자신이 부여받은 번호를 의미한다.
    # n은 전체리스트의 길이를 의미한다.
    i = 0
    while True:
        # 현재 부여받은 번호 길이에서 앞뒤로 범위안에 있고, 팰린드롬이라면 바꾼다.
        if 0< m-i <=n and 0< m+i<=n and l[m-i]==l[m+i]:
            if l[m-i]==1:
                l[m-i] = 0
                l[m+i] = 0
            else:
                l[m+i] = 1
                l[m-i] = 1
            i += 1
        else:
            break
    return l



# n은 스위치의 개수를 의미한다.
n = int(sys.stdin.readline())

# 스위치의 초기 상태가 담긴 리스트가 입력된다.
default = list(map(int,sys.stdin.readline().split()))
# 인덱스 정보를 맞추기 위해서 0번 인덱스를 만들어준다.
default.insert(0,0)

# 학생수의 정보가 입력된다.
students = int(sys.stdin.readline())
# 학생수만큼 변화에 대한 정보가 들어온다.
change = [list(map(int, sys.stdin.readline().split())) for _ in range (students)]

for j in range(students):
    number = change[j][1]
    if change[j][0] == 1:
        boy(number, n, default)
    else:
        girl(number, n, default)

for k in range(1, n+1, 20):
    print(*default[k:k+20])
