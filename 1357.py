# 삼각형 출력하기 기출변형2
# n이 입력된다
# 별이 하나씩 늘어나다가 n개가 됐을 시점부터
# 별이 하나씩 줄어든다.

#일반 삼각형 출력하는 코드까지 짜고
# 그 밑으로는 하나씩 줄어드는 코드를 짜면 되나?

n = int(input())

for i in range(1,n+1):
    for j in range(i):
        print('*', end="")
    print(" ")      #여기 까지가 일반 삼각형 출력하는 식


for i in range(n):
    print((n-i-1)*'*')