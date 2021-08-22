class Calculadora2:
    def __init__(self):
        pass

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b


calculadora = Calculadora2()
print("Soma: {}".format(calculadora.soma(1, 2)))
print("Subtração: {}".format(calculadora.subtracao(2, 3)))
print("Multiplicação: {}".format(calculadora.multiplicacao(4, 5)))
print("Divisão: {}".format(calculadora.divisao(6, 7)))
