# 5개의 정수를 입력받는다.
# 입력한 정수 중 최댓값을 첫째줄에 출력한다
# 입력한 정수 중 최솟값을 둘째줄에 출력한다

# 1. 각기 다른 변수에 입력받는다
# 2-1. 입력받는 숫자를 반복문을 통해 입력받고 그 수들을 리스트로 나열한다..?
# 2-2. 리스트 안의 수들을 순차적으로 재 배열한다.
# 2-3. 정수형으로 바꾸고 [0]번째 숫자와 [4]번째 숫자를 출력한다.
list1 = []
for i in range(5):
    n = int(input())
    list1.append(n)

list1.sort()

print(list1[4])
print(list1[0])