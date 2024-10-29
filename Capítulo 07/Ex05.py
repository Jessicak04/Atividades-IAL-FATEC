#5. Remove a instrução break e a instrução continue do laço de repetição abaixo:
#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#posicao = 0
#while posicao < len(numeros):
#    posicao += 1
#    if posicao == 3:
#        continue
#    elif posicao == 6:
#        break
#    print(numeros[posicao-1])

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
posicao = 0
while posicao < 5:
    if posicao != 2:
        print(numeros[posicao])
    posicao += 1