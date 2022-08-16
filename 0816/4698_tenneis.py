def is_primenumber(n):
    m = int(n**0.5)
    # 우선 길이가 n+1이고, 전부 소수라고 가정한 리스트를 만든다.
    prime_list = [True] * (n+1)
    for i in range(2, m+1):
        for j in range(i+i, n+1, i):
            prime_list[j] = False
    return [k for k in range(2, n+1) if prime_list[k]==True]

# 100만까지의 소수를 담은 arr 리스트를 먼저 만든다.
arr = is_primenumber(1000000)

T = int(input())
for tc in range(1,T+1):
    d,a,b = map(int, input().split())
    cnt = 0
    # a이상, b이하의 소수를 먼저 찾는다.
    for i in arr:
        if a<= i <= b:
           if str(d) in str(i):
               cnt += 1
    print(f"#{tc} {cnt}")
