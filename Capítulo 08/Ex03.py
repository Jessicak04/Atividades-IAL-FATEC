#3. Utilize a lista de compras do programa anterior para identificar qual o produto 
# mais barato e qual o produto mais caro da lista de compras.
#mais_barato = None
#mais_caro = None
#indice = 0
#while indice < len(lista_compras):
#    item_compra = lista_compras[indice]
#    if indice == 0:
#        mais_caro = item_compra
#        mais_barato = item_compra
#    else:
#        if item_compra["preço"] > mais_caro["preço"]:
#            mais_caro = item_compra

#        if item_compra["preço"] < mais_barato["preço"]:
#            mais_barato = item_compra

#    indice = indice + 1

#print("Produto mais caro: ", mais_caro["descrição"], "por", mais_caro["preço"],"reais")
#print("Produto mais barato: ", mais_barato["descrição"], "por", mais_barato["preço"],"reais")

mais_barato = None
mais_caro = None
indice = 0
while indice < len(lista_compras):
    item_compra = lista_compras[indice]
    if indice == 0:
        mais_caro = item_compra
        mais_barato = item_compra
    else:
        if item_compra["preço"] > mais_caro["preço"]:
            mais_caro = item_compra

        if item_compra["preço"] < mais_barato["preço"]:
            mais_barato = item_compra

    indice = indice + 1

print("Produto mais caro: ", mais_caro["descrição"], "por", mais_caro["preço"],"reais")
print("Produto mais barato: ", mais_barato["descrição"], "por", mais_barato["preço"],"reais")