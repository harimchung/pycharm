
def is_primenumber(n):
    m = int(n**0.5)
    arr = [True]*(n+1)
    for i in range (2, m+1):
        for j in range (i+i, n+1, i):
            arr[j] = False
    return [k for k in range(2,n+1) if arr[k]==True]

array = is_primenumber(1000)

T = int(input())
for tc in range(1,T+1):
    number = int(input())
    add_list = []
    for j in array:
        if j < number:
            add_list.append(j)

    count = 0
    # add_list에는 n보다 작은 숫자들이 생긴다
    n = len(add_list)
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if add_list[i] + add_list[j] + add_list[k] == number:
                    count += 1
    print(f"#{tc} {count}")
