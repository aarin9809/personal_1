#10개의 숫자를 차례대로 입력받은 후
#k번째 숫자가 입력이 된다
#k번째 숫자를 출력하면된다.
#예를들어 3번째 숫자를 출력하려면 k-1번째 리스트 요소값을 출력해야
#하는 것이다.

list1 = list(input().split())
k = int(input())

print(list1[k-1])