# a = int(input("Digite o primeiro valor: "))
# b = int(input("Digite o segundo valor: "))
# c = int(input("Digite o terceiro valor: "))
#
# if a > b and a > c:
#     print("O maior número é: {maiorNumero}".format(maiorNumero=a))
# elif b > a and b > c:
#     print("O maior número é: {maiorNumero}".format(maiorNumero=b))
# else:
#     print("O maior número é: {maiorNumero}".format(maiorNumero=c))

# a = int(input("Entre com um valor: "))
# b = int(input("Entre com um segundo valor: "))
#
# resto_a = a % 2
# resto_b = b % 2
#
# if a % 2 == 0 or b % 2 == 0:
#     print("Ao menos um dos números digitados é par.")
# else:
#     print("Ambos números são ímpares.")

nota1 = int(input("Nota do primeiro bimestre: "))
nota2 = int(input("Nota do segundo bimestre: "))
nota3 = int(input("Nota do terceiro bimestre: "))
nota4 = int(input("Nota do quarto bimestre: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
    print("Média do aluno: {}".format(media))
else:
    print("Foi informada alguma nota errada.")

