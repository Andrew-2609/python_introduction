def listar_letras(palavra):
    lista_letras = []

    for letra in palavra:
        lista_letras.append(letra)

    return lista_letras


def contar_letras(palavra):
    contador = 0

    for _ in palavra:
        contador += 1

    return "A quantidade de letras na palavra '{}' é: {}".format(palavra, contador)


if __name__ == '__main__':
    print(listar_letras("Chuva"))
