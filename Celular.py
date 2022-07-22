# Eu vou criar uma algo bem basico inicialmente
# quero apenas testar
# uma classe de celular
# Regras:
# Precisa ser possivel adicionar uma informacao, n e bom deixar o codigo muito estatico
# o valor dado precisa ser em float, dificilmente um produto tem um valor fechadinho
# dividir a responsabilidade das tarefas no maximo de def que eu conseguir
# e bom deixar o codigo legivel
# #

class Cell:

    def start(self):
        self.phone_information()
        self.sale()

    def sale(self):
        self.discount_application()
        print(
            """The value of the cell phone is {}$, but with 
            the \n discount of {}% he stay for {:.2f}$

            """
            .format(self.value, self.discount, self.value_descount))

    def discount_application(self):
        product_value = float(input('Qual o valor do produto?'))
        self.value = product_value

        discount_value = int(input('Qual o valor do desconto a ser aplicado?'))
        self.discount = discount_value

        self.value_descount = self.value-(self.discount/100*self.value)

    def phone_information(self):
        self.phone_information_input()
        print(""""
    Model: {}, 
    touchpad: {},  
    button: {} 
            """.format(self.brand, self.touchpad, self.button))

    def phone_information_input(self):
        brand_input = input("Qual a marca do celular? \n")
        touchpad_input = input("O celular tem touchpad? \n")
        button_input = input(" O celular tem botão?")

        self.brand = brand_input
        self.touchpad = touchpad_input
        self.button = button_input


celular = Cell()
celular.start()
