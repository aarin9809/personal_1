#역삼각형 출력하기 기출변형
# n=5 면 첫줄에는 별 5개가 찍히고
# 둘째줄에는 공백 1 별 4개가 찍힘
# 셋째줄에는 공백 2 별 3개가 찍힘
# 넷째줄에는 공백 3 별 2개가 찍힘
# 다섯째줄에는 공백 4 별 1개가 찍힘

#공백을 늘리려면 어떻게 해야하는가?
#라인을 거듭해 나갈수록 공백의 수를 1씩 늘리고 별의 숫자를 1씩 줄인다.

n = int(input())

for i in range(n): #0부터 n까지
     print(' '*i + '*' * (n-i))