from os import system as sys

def test():

    oosa = ['B','E','S']

    pato = 'pato'
    while True:
        resposta = input('').upper()
        oosa_2 = [x for x in oosa if resposta in x]
        if oosa_2 != list(resposta):
            oosa.append(resposta)
            print('letra nova')
        else:
            print('letra repetida')
            sys('cls')
            break
    return 'end'



#print(test())
a = input('    ')
b = ['a']
if b == list(a[0][0]):
    b.append(a[0][0])
    print('pato')
    print(b)