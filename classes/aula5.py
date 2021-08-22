numeros = [1, 3, 5, 7]
animais = ["cachorro", "gato", "elefante"]

animal = input("Digite o nome de um animal: ").casefold()

if animal in animais:
    print("\nEsse animal existe na lista!")
else:
    print("\nEsse animal não existe na lista! Adicionando-o ao registro...")
    animais.append(animal)
    print("\nAnimal adicionado com sucesso! Nova lista: {}".format(animais))
