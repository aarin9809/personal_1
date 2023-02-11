a, b = input().split()

a = int(a)
b = int(b)

if b % a == 0:
    x = b / a
    x = int(x)
    print(f'{a}*{x}={b}')
elif a % b == 0:
    x = a / b
    x = int(x)
    print(f'{b}*{x}={a}')
else:
    print('none')