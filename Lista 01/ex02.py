while True:
    # Solicita a entrada do usuário
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    if numero > 100:
        print("O número deve ser menor ou igual a 100.")
        continue
        # Imprime os números de 3 em 3 a partir do número, até 100
    for i in range(numero, 101, 3):
        print(i)
        # Pergunta se o usuário deseja digitar outro número
        resposta = input("Deseja digitar outro número? (sim/não): ")
    if resposta != 'sim':
        print("Processo encerrado.")
        break