#8-Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas: 
# • Qual o seu time de coração? 1-Fluminense; 2-Botafogo; 3-Vasco; 4-Flamengo; 
# 5-Outros • Onde você mora? 1-RJ; 2-Niterói; 3-Outros • Qual o seu salário? 
# Faça um programa que imprima: • o número de torcedores por clube; • a média 
# salarial dos torcedores do Botafogo; • o número de pessoas moradoras do Rio de 
# Janeiro, torcedores de outros clubes; • o número de pessoas de Niterói torcedoras 
# do Fluminense

torcedores = {
    "Fluminense": 0,
    "Botafogo": 0,
    "Vasco": 0,
    "Flamengo": 0,
    "Outros": 0
}

salarial_botafogo = []  
moradores_rj_outras = 0  
moradores_niteroi_fluminense = 0  

num_pessoas = int(input("Quantas pessoas participaram da pesquisa? "))

for _ in range(num_pessoas):
    time = int(input("\nQual o seu time de coração? (1-Fluminense; 2-Botafogo;3-Vasco; 4-Flamengo; 5-Outros): "))
    local = int(input("Onde você mora? (1-RJ; 2-Niterói; 3-Outros): "))
    salario = float(input("Qual o seu salário? "))

    # Contagem de torcedores por clube
    if time == 1:
        torcedores["Fluminense"] += 1
        if local == 2:  # Morador de Niterói
            moradores_niteroi_fluminense += 1
    elif time == 2:
        torcedores["Botafogo"] += 1
        salarial_botafogo.append(salario)
    elif time == 3:
        torcedores["Vasco"] += 1
    elif time == 4:
        torcedores["Flamengo"] += 1
    elif time == 5:
        torcedores["Outros"] += 1
        if local == 1:  # Morador do RJ
            moradores_rj_outras += 1

if local == 1 and time == 5:
    moradores_rj_outras += 1

print("\nNúmero de torcedores por clube:")
for time, count in torcedores.items():
    print(f"{time}: {count} torcedor(es)")

if salarial_botafogo:
    media_salarial_botafogo = sum(salarial_botafogo) / len(salarial_botafogo)
    print(f"\nMédia salarial dos torcedores do Botafogo: R$ {media_salarial_botafogo:.2f}")
else:
    print("\nNão há torcedores do Botafogo para calcular a média salarial.")

print(f"Número de moradores do Rio de Janeiro torcedores de 'Outros': {moradores_rj_outras}")
print(f"Número de moradores de Niterói torcedores do Fluminense: {moradores_niteroi_fluminense}")
