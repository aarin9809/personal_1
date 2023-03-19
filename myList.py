import random

def ListSize(List):
    i = 0
    while List[i] != None:
        i+=1
    return i

def addAt1(List, word, index):
    size = ListSize(List) # get List's size
    #print("size", size)
    for i in reversed(range(index, size+1)):
        List[i] = List[i-1]

    List[index] = word
    #print(List)

List = []

List = [None for _ in range(20)]

for i in range(0, 8):
    List[i] = random.randint(0,30)

print("초기 리스트:", List)
#List[8] = 'a'
addAt1(List, 'a', 8)


#List[9] = List[8]

#List[8] = 'b'
addAt1(List, 'b', 8)



# List[10] = List[9]
#
# List[9] = List[8]
#
# List[8] = 'c'

# i = 10
# while i>=8:
#     List[i] = List[i-1]
#     i-=1
# List[8] = 'c'
addAt1(List, 'c', 8)

# for i in reversed(range(5,12)):
#     List[i] = List[i-1]
#
# List[5] = 'd'
addAt1(List, 'd', 5)

# i = 12
# while i >= 1:
#     List[i] = List[i-1]
#     i-=1
# List[0] = 'e'
addAt1(List, 'e', 0)


# List[13] = List[12]
# List[12] = List[11]
# List[11] = List[10]
# List[10] = List[9]
# List[9] = List[8]
# List[8] = List[7]
# List[7] = List[6]
# List[6] = List[5]
# List[5] = List[4]
# List[4] = List[3]
# List[3] = List[2]
# List[2] = List[1]
# List[1] = 'f'

# for i in reversed(range(2,14)):
#     List[i] = List[i-1]
#
# List[1] = 'f'
addAt1(List, 'f', 1)



print(List)

