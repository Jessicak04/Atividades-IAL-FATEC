#5-Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as 
# caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200 volumes, 
# assim, esta transportadora precisa controlar a quantidade e o peso dos volumes para 
# acomodar nos caminhões. Faça um programa que leia n caixas e seu peso, ao final, 
# o programa deve imprimir a quantidade de volumes, o peso total dos volumes e o 
# peso médio dos volumes.

quantidade_volumes = 0
peso_total = 0.0
peso_maximo = 10.0  # em toneladas
max_volumes = 200

while quantidade_volumes < max_volumes:
    peso_caixa = float(input("Digite o peso da caixa (em toneladas, ou 0 para encerrar): "))
    if peso_caixa == 0:
        break
    if peso_caixa < 0:
        print("Peso inválido! Por favor, insira um peso positivo.")
        continue

    quantidade_volumes += 1
    peso_total += peso_caixa
    if peso_total > peso_maximo:
        print("Limite de peso excedido! O caminhão não pode carregar mais caixas.")
        break

if quantidade_volumes > 0:
    peso_medio = peso_total / quantidade_volumes
else:
    peso_medio = 0

print(f"\nQuantidade de volumes: {quantidade_volumes}")
print(f"Peso total dos volumes: {peso_total:.2f} toneladas")
print(f"Peso médio dos volumes: {peso_medio:.2f} toneladas")
