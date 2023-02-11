# 15초마다 온도 측정
# 최소, 최대 두개 정수 입력 후 장치 제공 정수 읽음
# 장치의 끝 -999
# 범위의 끝과 끝 최솟값과 최댓값이 같아도된다 -> N t R
# 위험수준 도달 -> Alert!


a, b = input().split()
a = int(a)
b = int(b)
deg = input().split()


while 0 < len(deg):
    if a <= deg <= b:
        print("Nothing to report")

    elif deg < a or deg > b:
        print("Alert!")
        break

    elif deg == -999:
        break