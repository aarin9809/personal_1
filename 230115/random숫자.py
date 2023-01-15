import random
a1 = random.randint(1,9)
a2 = random.randint(1,9)
a3 =  random.randint(1,9)
while a1 == a2:  # 중복
    a2 = random.randint(1,9)
while a3 == a1 or a3 == a2:
    a3 = random.randint(1,9)