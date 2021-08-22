def contador_letras(palavra): return [letra for letra in palavra]


calculadora = {
    'soma': lambda a, b: "{a} + {b} = {result}".format(a=a, b=b, result=a + b),
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

if __name__ == '__main__':
    print(contador_letras("Regen"))

    soma = calculadora['soma']

    print(soma(5, 9))
