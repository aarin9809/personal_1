# 두 실수 a, b가 입력됨
# 두 수를 사칙연산해서 그 중 가장 큰 수를 출력하시오

a, b = input().split()

a = float(a)
b = float(b)

big = max(a,b)
small = min(a,b)

result = max(big+small, big - small, big * small, big / small, small**big)

print(f'{result:.6f}')