cro = ['dz=', 'c=','c-','d-','lj','nj','s=','z=']
n = len(cro)

input_string = input()
s = len(input_string)
cnt = 0
i = 0

while i < s:

    if input_string[i:i+3] in cro:
        cnt += 1
        i += 3

    elif input_string[i:i+2] in cro:
        cnt += 1
        i += 2

    else:
        cnt += 1
        i += 1


print(cnt)

