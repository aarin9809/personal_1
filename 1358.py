# 삼각형 별찍기 기출변형3

# n이 주어진다
# n은 제일 밑변의 별 갯수이다
# 제일 밑변의 갯수부터 윗줄로 올라갈수록 별이 2개씩 없어지며 공백이 1칸씩 생긴다.

n = int(input())

print(" " , '*' * (n-4))
print("", '*' * (n-2))
print('*' * n)

#공백은 하나씩 줄어들고, 별은 2개씩 늘어난다.

for i in range(n):
    for j in range(n):
