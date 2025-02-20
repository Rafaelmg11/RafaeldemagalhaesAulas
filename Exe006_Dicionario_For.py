vendas_tecnologia = {'iphone':15000,'samsung galaxy':12000,'Tv Samsung':10000,'PS5':14300,'Tablet':1720,'Ipad':1200}

#demonstrando for
for chave in vendas_tecnologia:
    print(chave) #Imprimindo as chaves

print()

#Imprimindo as chaves e os valores:
for chave in vendas_tecnologia:
    print("O produto {} vendeu {} unidades.".format(chave,vendas_tecnologia[chave]))
    
print()

#Imprimindo as chaves e os valores:
for item in vendas_tecnologia.items():
    print(item)

print('')

#UNPACKING
for produto,vendas in vendas_tecnologia.items():
    print("{}: {} de unidades".format(produto,vendas))

