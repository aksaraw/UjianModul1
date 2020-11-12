class Statistic:

    # def cekInteger(nilai):
    #     hasil = False
    #     i = 0
    #     while i<=len(nilai)-1 and hasil == False:
    #         if ord(0) <= ord(nilai[i]) <= ord('9'):
    #             hasil = False
    #         else:
    #             hasil = True
    #         i+=1
    #     return hasil


    def mean(self, nilai):
        a = 0
        for i in nilai:
            a+=i
        
        rata = a/len(nilai)
        print(rata)
    
    def median(self, nilai):
        nilai.sort()
        # print(nilai) #value checker
        if len(nilai)%2 == 0:
            # print('genap') #value checker
            indexmed1 = (len(nilai)//2)-1
            # print(indexmed1) #value checker
            indexmed2 = len(nilai)//2 
            # print(indexmed2) #value checker
            med = (nilai[indexmed1] + nilai[indexmed2])/2
            print(med)
        else:
            # print('ganjil') #value checker
            indexmed = len(nilai)//2
            med = nilai[indexmed]
            print(med)

    def mode(self, nilai):
        jumlah = []
        for i in range(10):
            a = nilai.count(i)
            jumlah.append(a)
        # print(jumlah) #value checker
        tertinggi = max(jumlah)

        def indexCheck(jumlah,tertinggi):
            indexno = []
            for i in range(len(jumlah)):
                a = jumlah[i]
                if a == tertinggi:
                    indexno.append(i)
            return indexno

        indextertinggi = indexCheck(jumlah,tertinggi)
        # print(indextertinggi) #value checker
        
        if len(indextertinggi) == 1:
            print(indextertinggi[0])
        else:
            print('tidak ada modus')


st = Statistic()

st.mean([7,3,18])
st.median([9,5,3,6,7,10,100,8])
st.mode([0,4,4,6,4,5,5,7,5,5])