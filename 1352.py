#사각형 출력하기
n = int(input())
#
#for i in range(n):



for i in range(n): #0부터 n까지 반복 세로줄 반복
    for j in range(n): #0부터 n까지 반복 가로줄 반복해서 별찍기
        print('*', end="") # 별찍기 공백없이
    print("") #개행