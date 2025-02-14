produtos = ['apple','tv','mc','iphone x','IPad','apple watch','mac book','airpods']
novos_produtos = ['chromecast','windows phone']
produtos.extend(novos_produtos)
print(produtos)

print("")

print("Usando +:")
produtos = ['apple','tv','mc','iphone x','IPad','apple watch','mac book','airpods']
novos_produtos = ['chromecast','windows phone']
produtos_compilado = produtos + novos_produtos
print(produtos_compilado)

print("")

print("Usando Append:")
produtos.append(novos_produtos)
print(produtos)