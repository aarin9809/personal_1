def push(stack, data):
    stack.append(data) # 스택 후미에 data 삽입

def size(stack):
    return len(stack)

def top(stack):
    if empty(stack):
        return 'empty'
    return size(stack)

def pop(stack):
    if size(stack) != 0:
        stack.pop()

def empty(stack):
    if size(stack) == 0:
        return True
    else:
        return False

def menu():
    print("stack 사용법에 대해 설명드리겠습니다.")
    print("각각의 번호를 눌러서 스택을 사용해보세요!")
    print("스택 push 명령어:1 데이터")
    print("스택 pop 명령어:2")
    print("스택 top 명령어:3")
    print("스택 size 명령어:4")
    print("스택 empty 명령어:5")
    print("종료 명령어:6")
    print(">>>", end="")

class Stack():
    def __init__(self):
        print("stack 객체 생성")
        self.data = []

    def push(self, d):
        self.data.append(d)  # 스택 후미에 data 삽입

    def size(self):
        return len(self.data)

    def top(self):
        if self.empty():
            return 'empty'
        return self.size()

    def pop(self):
        if self.size() != 0:
            self.data.pop()

    def empty(self):
        if self.size() == 0:
            return True
        else:
            return False


def 절차지향스택():
    stack = []
    while (True):
        menu()
        cmd = input().split()
        # 명령어 인자가 2개 일 때
        if len(cmd) == 2 and cmd[0] == "1":
            print(f'stack에 {cmd[1]}을 삽입')
            push(stack, cmd[1])
        elif len(cmd) == 1:
            if cmd[0] == "2":
                if empty(stack):
                    print("삭제 불가능합니다.")
                else:
                    print("스택의 데이터 삭제")
                    pop(stack)
            if cmd[0] == "3":
                print("현재 stack의 top: ", top(stack))
            if cmd[0] == "4":
                print("현재 stack의 size: ", size(stack))
            if cmd[0] == "5":
                print("현재 stack의 empty 여부: ", empty(stack))
            if cmd[0] == "6":
                print("종료")
                break


def 객체지향스택():
    stack = Stack()
    while (True):
        menu()
        cmd = input().split()
        # 명령어 인자가 2개 일 때
        if len(cmd) == 2 and cmd[0] == "1":
            print(f'stack에 {cmd[1]}을 삽입')
            stack.push(cmd[1])

        elif len(cmd) == 1:
            if cmd[0] == "2":
                if stack.empty():
                    print("삭제 불가능합니다.")
                else:
                    print("스택의 데이터 삭제")
                    stack.pop()
            if cmd[0] == "3":
                print("현재 stack의 top: ", stack.top())
            if cmd[0] == "4":
                print("현재 stack의 size: ", stack.size())
            if cmd[0] == "5":
                print("현재 stack의 empty 여부: ", stack.empty())
            if cmd[0] == "6":
                print("종료")
                break
# main 함수
if __name__ == "__main__":
    #절차지향스택()
    객체지향스택()
















# stack = []
#
# stack.append(1) # [1]
# stack.append(2) #[1,2]
# stack.append(3) #[1,2,3]
#
# stackSize = len(stack)
# print(stack[stackSize-1]) # 3
#
# stack.pop()
# stackSize = len(stack)
# print(stack[stackSize-1])

