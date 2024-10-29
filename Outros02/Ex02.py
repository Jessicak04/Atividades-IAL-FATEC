#2- Entrar com o nome e salário  de um funcionário. Sabendo-se que o índice de 
# reajuste é de 8 %. Calcular o novo salário. Imprimir Nome, o salário e o novo 
# salário. Pergunte se deseja fazer novos cálculos. Se a resposta for não, encerrar 
# o programa. Se for sim começar novamente pedindo nome e fazendo novos cálculos.

while True:
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    reajuste = 0.08  # 8%
    novo_salario = salario * (1 + reajuste)

    print(f"\nNome: {nome}")
    print(f"Salário atual: R$ {salario:.2f}")
    print(f"Novo salário com reajuste: R$ {novo_salario:.2f}\n")

    resposta = input("Deseja fazer novos cálculos? (sim/não): ").strip().lower()
    if resposta != 'sim':
        print("Programa encerrado.")
        break
