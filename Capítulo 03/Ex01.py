#1. Faça um algoritmo que solicite 3 notas para o usuário, calcule a média e indique 
# se o aluno foi aprovado ou reprovado (nota precisar ser maior ou igual à sete para 
# o aluno ser aprovado).

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = ( nota1 + nota2 + nota3 ) / 3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")