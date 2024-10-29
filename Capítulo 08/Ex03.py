#3. Utilize a lista de compras do programa anterior para identificar qual o produto 
# mais barato e qual o produto mais caro da lista de compras.

lista_compras = [
    {"descrição": "Café", "preço": 5.00},
    {"descrição": "Leite", "preço": 4.00},
    {"descrição": "Pão", "preço": 6.00},
    {"descrição": "Caneca", "preço": 19.00},
    {"descrição": "Chocolate", "preço": 6.50},
]

for item_compra in lista_compras:
    print("Produto:", item_compra["descrição"], 
     "por", str(item_compra["preço"]), "reais.")
    
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