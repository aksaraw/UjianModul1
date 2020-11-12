nomor = list(input('Input your phone number: '))

def create_phone_number(a):
    def cekAlphabet(nomor):
        hasil = False
        i = 0
        while i<=len(nomor)-1 and hasil == False:
            if ord('A') <= ord(nomor[i]) <= ord('Z') or ord('a') <= ord(nomor[i]) <= ord('z'):
                hasil = True
            else:
                hasil = False
            i+=1
        return hasil
    
    def cekSymbol(nomor):
        hasil = False
        i = 0
        while i<=len(nomor)-1 and hasil == False:
            if ord(' ') <= ord(nomor[i]) <= ord('/') or ord(':') <= ord(nomor[i]) <= ord('@') or ord('[') <= ord(nomor[i]) <= ord('`') or ord('{') <= ord(nomor[i]) <= ord('ÿ'):
                hasil = True
            else:
                hasil = False
            i+=1
        return hasil

    if len(a) != 10:
        print('Digits must be in length of 10, not more or less')
    elif '-' in nomor:
        print('Input only positive number')
    elif cekAlphabet(nomor):
        print('Invalid input. No alphabet.')
    elif cekSymbol(nomor):
        print('Invalid input. No symbols.')
    else:
        nomor.insert(0,'(')
        nomor.insert(4,') ')
        nomor.insert(8,'-')
        print(''.join(nomor))

create_phone_number(nomor)
