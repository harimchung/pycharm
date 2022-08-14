import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

def is_prime_number2(n):
    table = [True]*(n+1)
    m = int(n**0.5)
    for i in range (2,m+1):
        if table[i]:
            for j in range(i+i, n+1, i):
                table[j] = False
    return [i for i in range(2,n+1) if table[i]==True]

table_b = is_prime_number2(b)

for i in table_b:
    if a <= i <= b:
        print(i)

