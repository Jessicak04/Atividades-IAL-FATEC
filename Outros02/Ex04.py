# 4-Dado um número secreto adotado inteiro = 98. O usuário deverá digitar um número 
# até acertar o número secreto. Enquanto a pessoa não acertar, o programa ficara em 
# loop. Se a pessoa não acertou, emita uma mensagem de aviso.  Quando a pessoa 
# acertar emita uma mensagem dando  parabéns ao usuário.

# Número secreto
numero_secreto = 98

# Loop para solicitar palpites até que o usuário acerte
while True:
    # Solicita que o usuário digite um número
    palpite = int(input("Digite um número: "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        break  # Sai do loop se o palpite estiver correto
    else:
        print("Número incorreto. Tente novamente.")
