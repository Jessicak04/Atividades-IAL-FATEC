#3-Crie um programa que leia o preço de compra e o preço de venda de 10 mercadorias. 
# Para cada mercadoria verificar imprimir se houve lucro e se o lucro foi maior que 
# 15%. Acumule o valor total de mercadorias compradas.

total_comprado = 0
for i in range(1, 11):
    print(f"\nMercadoria {i}:")
    preco_compra = float(input("Digite o preço de compra: R$ "))
    preco_venda = float(input("Digite o preço de venda: R$ "))

    total_comprado += preco_compra

    if preco_venda > preco_compra:
        lucro = preco_venda - preco_compra
        percentual_lucro = (lucro / preco_compra) * 100

        print(f"Houve lucro de R$ {lucro:.2f} ({percentual_lucro:.2f}%)")
        
        if percentual_lucro > 15:
            print("O lucro foi maior que 15%.")
    else:
        print("Não houve lucro.")

print(f"\nValor total de mercadorias compradas: R$ {total_comprado:.2f}")
