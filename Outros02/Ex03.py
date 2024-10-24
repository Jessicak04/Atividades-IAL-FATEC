#3-Crie um programa que leia o preço de compra e o preço de venda de 10 mercadorias. 
# Para cada mercadoria verificar imprimir se houve lucro e se o lucro foi maior que 
# 15%. Acumule o valor total de mercadorias compradas.

# Inicializa a variável para acumular o valor total de mercadorias compradas
total_comprado = 0

# Loop para ler os preços de 10 mercadorias
for i in range(1, 11):
    print(f"\nMercadoria {i}:")
    preco_compra = float(input("Digite o preço de compra: R$ "))
    preco_venda = float(input("Digite o preço de venda: R$ "))

    # Acumula o valor total de mercadorias compradas
    total_comprado += preco_compra

    # Verifica se houve lucro
    if preco_venda > preco_compra:
        lucro = preco_venda - preco_compra
        percentual_lucro = (lucro / preco_compra) * 100

        print(f"Houve lucro de R$ {lucro:.2f} ({percentual_lucro:.2f}%)")
        
        # Verifica se o lucro foi maior que 15%
        if percentual_lucro > 15:
            print("O lucro foi maior que 15%.")
    else:
        print("Não houve lucro.")

# Imprime o valor total de mercadorias compradas
print(f"\nValor total de mercadorias compradas: R$ {total_comprado:.2f}")
