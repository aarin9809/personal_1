lst = list()
lst.append(1)
lst.append(2)
lst.append('abc')
print(lst) #[1,2,'abc']

lst.insert(0,3)
lst.insert(2, 'world')
lst.insert(4,3)#지정위치로 지정요소 추가 기존요소는 뒤로 밀림
print(lst)
lst.remove(3)#앞에서부터 삭제
print(lst)
lst.pop(3)#지정위치 삭제
print(lst)
lst.pop()#맨 뒤 1개 삭제
print(lst)
print(len(lst))
lst3 = lst + lst
print(lst3)
lst4 = lst *4
print(lst4)
del lst4[4:]
print(lst4)


del lst4[1]
lst4.sort()
print(lst4)
lst4.reverse()
print(lst4)
print(lst4.count(1))