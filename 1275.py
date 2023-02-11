# n을 입력받는다 k도 입력받는다
# k는 n의 제곱역할을한다.
# 다시 말해, n을 k번 반복해서 곱하는 반복문을 만드는 문제다.
# 예를 들어 n=3 k =4 일때, 3을 4번 반복한 결과를 찍어내면 된다.
n, k = input().split()
n = int(n)
k = int(k)

for i in range(1,n):
    if n!=0 and k>=0:
        n ** k
print(n**k)


