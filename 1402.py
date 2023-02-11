# n개의 데이터가 입력이 된다.
# 둘째줄에는 데이터들이 입력된다.
# 입력된 데이터들을 리스트로 만들어 입력된 값을 넣는다
# 정수화 시켜서 거꾸로 출력한다.


n = int(input())

d = list(input().split())
new = list(map(int, d))
new.sort()
new.reverse()

for i in new:
    print(i, end=" ")