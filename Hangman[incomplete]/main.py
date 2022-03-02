# Hangman game. The objetive of this game is to randomly choose a word
# the player must find out which word was chosen #

#
# racunho 
# Desafios de completar essa aplicacao:
# Eu precisaria primeiro ter todas as palavras salvas, o melhor seria 
# salvar todas em outro arquivo txt ou .py tanto faz
# o numero de vidas e de 6, sendo necessario ter uma interface que mostre 
# o boneco se formando #


#Sera #

#imports
import random
from words import word_list

print(random.choice(word_list))
def start(random_word):
                letra_oculta = 1
                letra_oculta = len(random_word)*'*'
                contador = -1
                print(letra_oculta)
                letra = input('Uma letra')
                while True:
                    for i in random_word:
                        contador += 1
                        if i in letra:
                            letra_oculta = random_word[contador]
                            return letra_oculta
                    break

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