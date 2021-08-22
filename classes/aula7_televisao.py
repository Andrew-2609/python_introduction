class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            print("Desligando a televisão...")
            self.ligada = False
            return "A televisão está desligada."
        else:
            print("Ligando a televisão...")
            self.ligada = True
            return "A televisão está ligada."

    def aumentar_canal(self):
        self.canal += 1

    def diminuir_canal(self):
        self.canal -= 1


if __name__ == "__main__":
    televisao = Televisao()
    print(televisao.power())
    print(televisao.power())

    print("\nO canal atual é: {}".format(televisao.canal))
    televisao.aumentar_canal()
    televisao.aumentar_canal()
    print("O canal atual é: {}".format(televisao.canal))
    televisao.diminuir_canal()
    print("O canal atual é: {}".format(televisao.canal))
