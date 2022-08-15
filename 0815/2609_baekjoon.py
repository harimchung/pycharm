# a, b = map(int, input().split())
# if b > a:
#     a, b = b, a
#
# def gdp(a,b):
#     r = 0
#     while b > 0:
#         r = a % b
#         a = b
#         b = r
#     return a
# def ldp(a,b):
#     return a*b//gdp(a,b)
#
# print(gdp(a,b))
# print(ldp(a,b))

a = [1,2,3,4,5,5]
print(max(a))
print(a.count(max(a)))
print(a.index((max(a))))