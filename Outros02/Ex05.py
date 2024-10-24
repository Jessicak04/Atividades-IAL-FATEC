#5-Uma transportadora utiliza caminhões que suportam até 10 toneladas de peso, as 
# caixas transportadas tem tamanho fixo e o caminhão comporta no máximo 200 volumes, 
# assim, esta transportadora precisa controlar a quantidade e o peso dos volumes para 
# acomodar nos caminhões. Faça um programa que leia n caixas e seu peso, ao final, 
# o programa deve imprimir a quantidade de volumes, o peso total dos volumes e o 
# peso médio dos volumes.

# Inicializa as variáveis
quantidade_volumes = 0
peso_total = 0.0
peso_maximo = 10.0  # em toneladas
max_volumes = 200

# Loop para ler os pesos das caixas
while quantidade_volumes < max_volumes:
    peso_caixa = float(input("Digite o peso da caixa (em toneladas, ou 0 para encerrar): "))
    
    # Permite encerrar a entrada de caixas se o peso for 0
    if peso_caixa == 0:
        break
    
    # Verifica se o peso da caixa é válido
    if peso_caixa < 0:
        print("Peso inválido! Por favor, insira um peso positivo.")
        continue

    # Acumula a quantidade de volumes e o peso total
    quantidade_volumes += 1
    peso_total += peso_caixa
    
    # Verifica se o peso total excede o limite do caminhão
    if peso_total > peso_maximo:
        print("Limite de peso excedido! O caminhão não pode carregar mais caixas.")
        break

# Cálculo do peso médio
if quantidade_volumes > 0:
    peso_medio = peso_total / quantidade_volumes
else:
    peso_medio = 0

# Imprime os resultados
print(f"\nQuantidade de volumes: {quantidade_volumes}")
print(f"Peso total dos volumes: {peso_total:.2f} toneladas")
print(f"Peso médio dos volumes: {peso_medio:.2f} toneladas")
