#8-Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas: 
# • Qual o seu time de coração? 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 
# 5-Outros • Onde você mora? 1-RJ; 2-Niterói; 3-Outros • Qual o seu salário? 
# Faça um programa que imprima: • o número de torcedores por clube; • a média 
# salarial dos torcedores do Botafogo; • o número de pessoas moradoras do Rio de 
# Janeiro, torcedores de outros clubes; • o número de pessoas de Niterói torcedoras 
# do Fluminense

# Inicializa contadores e acumuladores
torcedores = {
    "Fluminense": 0,
    "Botafogo": 0,
    "Vasco": 0,
    "Flamengo": 0,
    "Outros": 0
}

soma_salario_botafogo = 0
contador_botafogo = 0
moradores_rj_outros = 0
moradores_niteroi_fluminense = 0

# Loop para coletar as respostas
while True:
    # Pergunta sobre o time de coração
    print("Qual o seu time de coração?")
    print("1 - Fluminense")
    print("2 - Botafogo")
    print("3 - Vasco")
    print("4 - Flamengo")
    print("5 - Outros")
    time = int(input("Digite o número correspondente: "))
    
    if time < 1 or time > 5:
        print("Opção inválida! Tente novamente.")
        continue
    
    # Contabiliza o time de coração
    if time == 1:
        torcedores["Fluminense"] += 1
    elif time == 2:
        torcedores["Botafogo"] += 1
        # Pergunta o salário se for do Botafogo
        salario = float(input("Qual o seu salário? R$ "))
        soma_salario_botafogo += salario
        contador_botafogo += 1
    elif time == 3:
        torcedores["Vasco"] += 1
    elif time == 4:
        torcedores["Flamengo"] += 1
    elif time == 5:
        torcedores["Outros"] += 1
    
    # Pergunta sobre a localização
    print("Onde você mora?")
    print("1 - RJ")
    print("2 - Niterói")
    print("3 - Outros")
    local = int(input("Digite o número correspondente: "))
    
    if local < 1 or local > 3:
        print("Opção inválida! Tente novamente.")
        continue
    
    # Contabiliza a localização
    if local == 1 and time == 5:
        moradores_rj_outros += 1
    elif local == 2 and time == 1:
        moradores_niteroi_fluminense += 1

    # Pergunta se deseja continuar
    continuar = input("Deseja continuar a pesquisa? (sim/não): ").strip().lower()
    if continuar != 'sim':
        break

# Resultados
print("\nResultados da pesquisa:")
print(f"Número de torcedores por clube:")
for time, quantidade in torcedores.items():
    print(f"{time}: {quantidade}")

if contador_botafogo > 0:
    media_salarial_botafogo = soma_salario_botafogo / contador_botafogo
    print(f"\nMédia salarial dos torcedores do Botafogo: R$ {media_salarial_botafogo:.2f}")
else:
    print("\nNão foram registrados torcedores do Botafogo.")

print(f"Número de pessoas moradoras do Rio de Janeiro, torcedores de outros clubes: {moradores_rj_outros}")
print(f"Número de pessoas de Niterói torcedoras do Fluminense: {moradores_niteroi_fluminense}")
