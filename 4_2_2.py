def stem_leaf(lst):
    d = {} #빈 딕셔너리

    #lst 원소 순회
    for num in range(lst):
        k = num // 10 #key(stem)
        v = num % 10  #value(leaf)
        
        if k not in d:
            d[k] = [v]  #create stem and value
        else:
            d[k].append(v)  #append leaf


    for k in sorted(d.keys()):
        d[k].sort()
        print(k, ":", d[k])

lst1 = [1,2,3,10,0,21,10]
lst2 = [111,20,30,40,55,66]

#key(10의 자리) : value[1,2,3]
#0


stem_leaf(lst1)

stem_leaf(lst2)