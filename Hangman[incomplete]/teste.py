import random
from words import word_list


def start(random_word):
                letra_oculta = 1
                letra_oculta = len(random_word)*'*'
                alfabeto = []
                print(letra_oculta)
                contador_2 = 7
                ss = False
                while True:
                    if letra_oculta == random_word:
                        return 'voce ganhou'

                    if ss == True:
                        
                        contador_2 -= 1
                        print('{} vidas'.format(contador_2))
                        if contador_2 == 0:
                            break
                        
                    contador = -1
                    letra = input('Uma letra')
                    
                    verificao = 0
                    
                        
                    
                    while True:
                        for i in random_word:
                            
                            contador += 1
                            if i in letra:
                                letra_oculta_2 = list(letra_oculta)
                                letra_oculta_2[contador] = letra
                                letra_oculta = "".join(letra_oculta_2)
                                verificao += 1
                                ss = False
                        if verificao == 0:
                            ss = True


                        print(letra_oculta)        
                            
                            
                        break
                return ':)'
                        

                    #
                    # fazer uma repeticao de for que substitua o valor
                    # poed funcionar#


while True:
    try:
        random_word = random.choice(word_list)
        answer = input('Deseja jogar?y/n')
        if answer.upper() == 'Y' or answer.upper() == 'N':
            print(start(random_word))
            break           
    except:
        print('algo deu errado')
        break