#90 글자 내로 된 문장이 입력된다.
#영어 소문자, 공백 및 특수문자로만 이루어져 있다.

#a-z까지 반복문으로 1차 돌면서 문장에 있는 철자들을 2차로 돌면서 검사?



str = input()

count = 0

d = {}
# 알파벳이 키값이 되도록 딕셔너리 초기화
for i in range(26):
    d[chr(ord('a') + i)] = 0

# str를 순회하면서 해당 알파벳을 키값으로 카운트
for i in str:
    #알파벳이 아닐때 처리안함
    if i < ord('a') or i > ord('z'):
        continue
    # 알파벳일때 처리
    d[i] += 1  # i = key , d[i] = value