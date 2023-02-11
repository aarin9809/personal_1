#n개의 숫자를 입력받고
#받은 숫자들을 두번 출력하시오

n = int(input()) #s에 몇개가 들어갈지 결정하는 수

s = input().split() #s 변수에 들어갈 수

for i in range(2):
    for j in range(n):
        print(s[j])