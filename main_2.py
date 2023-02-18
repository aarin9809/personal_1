def func(a, b):
    if a > b:
        return
    if a % 2 == 1:
        print(a, end=" ")
    func(a+1, b)

a, b = input().split()
func(int(a), int(b))