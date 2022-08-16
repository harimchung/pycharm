def is_palindrome(n):
    answer = "no"
    if n == n[::-1]:
        answer = "yes"
    return answer


while True:
    n = input()
    if n == "0":
        break
    print(is_palindrome(n))
