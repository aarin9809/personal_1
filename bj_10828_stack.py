#push X : 정수 x를 스택에 넣는 연산이다

#pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는
#경우에는 -1을 리턴한다

#size : 스택에 들어있는 정수의 개수를 출력한다.

#empty : 스택이 비어있으면 1, 아니면 0을 출력한다.

#top : 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는
# -1을 리턴한다.

# 첫째줄에는 명령의 수가 주어진다.
# 둘째줄부터 명령의 수만큼 명령이 하나씩 주어진다.

def push(stack, data):
    stack.append(data)
def pop():
    if size(stack) !=0:
        stack.pop()
def size():
    return len(stack)
def empty():
    if size(stack) == 0:
        return 1
    else:
        return 0
def top():
    if empty(stack):
        return -1
    return stack[-1]

n = int(input())
stack = []








if __name__ == "__main__":
    pass