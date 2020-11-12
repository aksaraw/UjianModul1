def moveZeros(masuk):
    def indexCheck(masuk):
        indexno = []
        for i in range(len(masuk)):
            a = masuk[i]
            if a == 0 and a is not False:
                indexno.append(i)
        return indexno
    
    jumlah0 = 0
    for i in masuk:
        if i == 0 and i is not False:
            jumlah0 += 1
    # print(jumlah0) #value checker

    index0 = indexCheck(masuk)
    index0.reverse()
    # print(index0) #value checker
    for i in index0:
        masuk.pop(i)
    
    for i in range(jumlah0):
        masuk.append(0)
    print(masuk)


moveZeros([False,1,0,1,2,0,1,3,'a'])
moveZeros([0,0,0,'Test',0,3,'a',True,False])
moveZeros([0,True,True,False,'a','b',1,1,1])

