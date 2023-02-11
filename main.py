n = int(input())

for i in range(1, n+1): #세로 반복 횟수
    for j in range(1, i+1): #가로 반복 횟수
        print('*' * j, end="") #가로로 j개 만큼 별이 찍힐 것임
    print("") #개행