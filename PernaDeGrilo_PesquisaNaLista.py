cliente = ['joao','luis','pedro','guilherme','gustavo']
telefone = [997433220,996065884,997730868,986543322,43125678]
bairro = ['comasa','vila da gloria','iririu','paraiso','aventureiro']

pesquisa = (input("Digite o nome de cliente que você deseja pesquisar: "))
pesquisa = pesquisa.lower()

if pesquisa in cliente:
    i = cliente.index(pesquisa)
    print ("Cliente: {}".format(cliente[i]))
    print("Telefone: {}".format(telefone[i]))
    print("Bairro: {}".format(bairro[i]))
else:
    print("Cliente não registrado")