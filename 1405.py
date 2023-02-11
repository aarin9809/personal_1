#n개의 숫자가 입력됨
#k에 숫자를 입력받음
#k에 받은 숫자들을 왼쪽으로 한칸씩 옮기면서 출력함.
#왼쪽으로 돌리는 횟수는 n번만큼 돌린다.

n = int(input())
d = list(input().split())
new = list(map(int, d)) #[1 2 3 4 5]
b = 0
# 맨 앞 수를 맨 뒤로 옮기는법?
#new 배열에서 [0]번째 요소를 맨 뒤로 append
#pop으로 [0]을 뽑아내고 그 수를 변수에 담아서 append로 그 변수를
#출력?
#a = new.pop(0)
#new.append(a)
#print(new)
#[2, 3, 4, 5, 1]
# 여기까지는 성공. 이 과정을 반복문으로 돌려보자.
# n이 5이므로 5번만 반복하면 된다

while n>b:
    print(*new,end=" ")
    print(sep='\n')
    a = new.pop(0)
    new.append(a)
    b+=1