#2. Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o 
# programa descrever se o usuário fará ou já fez 18 anos neste ano.

ano_nascimento = int (input ("Digite o ano que você nasceu: "))
idade = 2024 - ano_nascimento

if idade == 18:
    print("O usuário fará ou vez 18 anos este ano.")
elif idade > 18:
    print("O usuário já fez 18 anos.")
else:
    print("O usuário ainda não fez 18 anos.")