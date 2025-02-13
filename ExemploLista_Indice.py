#INDICE EM LISTAS
produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos[1])
print(produtos[4])

vendas = [1000,1500,350,270,900]
print("As vendas de {} foram de {}".format(produtos[1],vendas[1]))

#DESCOBRINDO O INDIDE DE X ITEM NA LISTA
produtos = ['tv','celular','mouse','teclado','tablet']
i = produtos.index("mouse")
print("O valor de i é "+ str(i))
print("O produto da posição i é " + str(produtos[i]))
