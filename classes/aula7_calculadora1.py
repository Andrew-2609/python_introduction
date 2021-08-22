class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b


if __name__ == "__main__":
    calculadora = Calculadora(10, 2)
    print("Soma: {}".format(calculadora.soma()))
    print("Subtração: {}".format(calculadora.subtracao()))
    print("Multiplicação: {}".format(calculadora.multiplicacao()))
    print("Divisão: {}".format(calculadora.divisao()))
