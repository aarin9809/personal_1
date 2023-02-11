#두 자연수 추가
a, b = input().split()

a = int(a)
b = int(b)

sum = 0

for i in range(a, b+1):
    if i % 2 == 0:
        print(-i, end="")
        sum -= i
    else:
        print(f'+{i}', end="")
        sum += i
print(f'={sum}')