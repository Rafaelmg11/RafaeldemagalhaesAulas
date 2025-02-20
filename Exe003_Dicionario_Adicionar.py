vendas_vendedores = {}


vendas_vendedores['Joao'] = 1500

print(vendas_vendedores)

#Adicionando na lista
vendas_vendedores.update({'Lira':50,'Nathalie':100})
print(vendas_vendedores)

#Atualizando 'Joao'
vendas_vendedores['Joao'] = 70
print(vendas_vendedores)
print("Fim do Programa")