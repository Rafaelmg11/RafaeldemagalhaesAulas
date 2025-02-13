faturamento = input("Qual foi o faturamento da loja nesse mês? ")
custo = input("Qual foi o custo da loja nesse mês? ")


if faturamento == "" or custo == "" :
    print("Os valores estão invalidos por favor, digite novamente")
    faturamento = input("Qual foi o faturamento da loja nesse mês? ")
    custo = input("Qual foi o custo da loja nesse mês? ")
    lucro = int (faturamento) - int (custo)
    print("O lucro da loja foi de {} R$".format(lucro))
else:
    lucro = int (faturamento) - int (custo)
    print("O lucro da loja foi de {} R$".format(lucro))

#CODIGO DO PROFESSOR:
#if faturamento != "" or custo != "" :
#    lucro = int (faturamento) - int (custo)
#    print("O lucro da loja foi de {} R$".format(lucro))
#else:
#    print("Algum valor não foi fornecido")

#CODIGO DO PROFESSOR
#if faturamento and custo:
#    lucro = int (faturamento) - int (custo)
#    print("O lucro da loja foi de {} R$".format(lucro))
#else:
#    print("Algum valor não foi fornecido")
