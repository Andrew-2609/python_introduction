from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import listar_letras, contar_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.power())

    print()

    calculadora = Calculadora(1, 10)
    print("A divisão de {a} por {b} é igual a: {result}".format(a=calculadora.a, b=calculadora.b,
                                                                result=calculadora.divisao()))

    print("\n{}".format(listar_letras("Regen")))
    print(contar_letras("Regen"))
