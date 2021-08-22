# number = int(input("Entre com um número: "))
#
# div = 0
#
# for x in range(1, number + 1):
#     resto = number % x
#     if resto == 0:
#         div += 1
#
# if div == 2:
#     print("\nO número {num} é primo".format(num=number))
# else:
#     print("\nO número {num} não é primo".format(num=number))

# number = int(input("Digite a range de números primos: "))
#
# for num in range(number + 1):
#     div = 0
#
#     for x in range(1, num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print(num)

nota = int(input("Digite uma nota para o aluno: "))

while nota > 10 or nota < 0:
    print("Nota inválida!")
    nota = int(input("Digite uma nota para o aluno: "))

print(nota)
