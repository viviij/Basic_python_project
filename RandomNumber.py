# acertar o numero escholido aleatoriamente
# numero maximo ter um limite para o jogo n ser impossivel
# jogo acaba quando acerta
# vida nao e necessaria
# focar no uso de def o resto se resume a repeticao

import random


class RandomNumber:
    print("O jogo é bem simples, um número sera escolhido aleatóriamente, basta acertar. Boa sorte!")

    def __init__(self):
        self.value = 0
        self.minimumValue = 0
        self.maximumValue = 100

        self.end = True

        self.attempts = 0

    def start(self):
        self.randomNumber()
        while self.end == True:
            self.attempts += 1
            answerValue = input('Diga um número')
            if int(answerValue) > self.value:
                print("Errou :( Valor muito alto")
            elif int(answerValue) < self.value:
                print("Errou  :( Valor muito baixo")
            elif int(answerValue) == self.value:
                print("Parabéns! Você precisou de um total de {} tentativas para acertar".format(
                    self.attempts))

            self.end == False

    def randomNumber(self):
        self.value = random.randint(self.minimumValue, self.maximumValue)


jogo = RandomNumber()

jogo.start()
