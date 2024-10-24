#1. Faça um programa que inicialize uma lista de compras com 5 itens 
# diferentes e exiba todos utilizando um laço de repetição while.

itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
posicao = 0
while posicao < len(itens_compra):
    print(itens_compra[posicao])
    posicao+=1