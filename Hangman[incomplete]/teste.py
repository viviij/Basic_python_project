import random
from time import sleep as t
from words import word_list
from os import system as sys

#Problemas restantes
# -ler aaaaaaaaaaaa E a da mesma forma na verificacao de 
# verdaeiro ou falso se a letra e repetida $Corrigido
# -ler toda letra em maisculo para n quebrar na verificacao $Corrigido
# -mudar o idioma do programa
# -organizar o codigo
# -enviar para o github#


def start(random_word):
                vida = 6
                letra_oculta = 1
                letra_oculta = len(random_word)*'*'
                alfabeto = []
                ss = False
                while True:
                    if letra_oculta == random_word:
                        return 'voce ganhou'
                    if ss == True:
                        print('Voce errou! {} tentativas restantes'.format(vida))
                        if vida == 0:
                            return 'voce perdeu'
                        
                    contador = -1
                    print(letra_oculta)
                    letra = input('Uma letra  ').upper()
                    alfabeto_2 = [x for x in alfabeto if letra[0][0] in x]

                    verificao = 0
                    if alfabeto_2 != list(letra[0][0]):
                        alfabeto.append(letra[0][0])
                        while True:
                            for i in random_word:
                                
                                contador += 1
                                if i in letra:
                                    letra_oculta_2 = list(letra_oculta)
                                    letra_oculta_2[contador] = letra[0]
                                    letra_oculta = "".join(letra_oculta_2)
                                    verificao += 1
                                    ss = False
                            if verificao == 0:
                                ss = True
                                vida -= 1

                            sys('cls')

                                   
                                
                                
                            break
                    elif alfabeto_2 == list(letra[0][0]):
                        print ('digite uma letra diferente! Voce ja tentou {}'.format(letra.upper()[0]))
                        t(5)
                        sys('cls')
                    
                
                        

                    #
                    # fazer uma repeticao de for que substitua o valor
                    # poed funcionar#


while True:
    try:
        random_word = random.choice(word_list)
        answer = input('Deseja jogar?y/n\n')
        if answer.upper() == 'Y':
            print(start(random_word))
            break
        if answer.upper() == 'N':
            print('Ah')
            break
    except:
        print('algo deu errado')
        break