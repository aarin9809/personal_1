# 연결리스트
class Node:
    def __init__(self, word):
        self.word = word
        self.next = None


# 연결 리스트의 마지막 위치에 새로운 단어를 추가하는 함수에요.
def add(List, word):
    while List.next != None:    #None 값을 찾을때까지 도는 반복문
        List = List.next        #다음 리스트로
    List.next = Node(word)      #None값에 도달했을 경우 word값을 다음 리스트에 추가


# 연결 리스트의 index 위치에 새로운 단어를 추가하는 함수에요.
def addAt(List, word, index):
    if index < 0:
        print(index, "에", word, "를 추가할 수 없습니다")
        return
    for i in range(index):
        List = List.next
        if List == None:
            print(index, "에", word, "를 추가할 수 없습니다")
            return

    # index 위치에 새로운 단어를 추가해 주세요.
    newNode = Node(word)        #newNode 객체 생성
    newNode.next = List.next    #newNode다음에 들어갈 데이터는 List에서 다음에 올 값
    List.next = newNode         #List다음에 올 값은 newNode 이다.


# 연결 리스트의 index 위치에 있는 단어를 제거하는 함수에요.
def deleteAt(List, index):
    if index < 0:
        print(index, "에서 단어를 제거할 수 없습니다")
        return
    for i in range(index):
        List = List.next
        if List == None:
            print(index, "에서 단어를 제거할 수 없습니다")
            return

    # index 위치에 있는 단어를 제거해 주세요.
    if List.next != None:
        List.next = List.next.next
    else:
        List.next = None


def printList(List):
    # 연결 리스트를 출력하는 함수에요. 수정하지 않아도 돼요.
    while List != None:
        print(List.word)
        List = List.next


def main():
    # 캐터필러의 단어장을 만드는 부분이에요. 고치지 않아도 돼요.
    List = Node("< 캐터필러의 단어장 >")

    while True:
        value = input()
        if value == "":
            break
        elif value.startswith("#"):
            continue
        elif value == "printList":
            printList(List)
        elif value.startswith("add "):
            add(List, value[4:])
        elif value.startswith("addAt "):
            value = value[6:].split()
            addAt(List, ''.join(value[:-1]), int(value[-1]))
        elif value.startswith("deleteAt "):
            deleteAt(List, int(value.split()[1]))
        else:
            print("잘못된 입력입니다.")


if __name__ == "__main__":
    main()