# 4-Dado um número secreto adotado inteiro = 98. O usuário deverá digitar um número 
# até acertar o número secreto. Enquanto a pessoa não acertar, o programa ficara em 
# loop. Se a pessoa não acertou, emita uma mensagem de aviso.  Quando a pessoa 
# acertar emita uma mensagem dando  parabéns ao usuário.

numero_secreto = 98

while True:
    palpite = int(input("Digite um número: "))
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break 
    else:
        print("Número incorreto. Tente novamente.")
