#TRANSFORMA APENAS A PRIMEIRA LETRA DE UMA STRING EM MAIUSCULA
nome = "rafael"
print(nome.capitalize(),"\n")


#TRANSFORMA TODAS AS LETRAS EM MINUSCULA
nome = "RAFAEL"
print(nome.casefold(),"\n")


#CONTA O NÚMERO DE VEZES QUE UM CARACTERE ESPECIFICO APARECE NA STRING
nome = "RafaelMagalhaes@gmail.com"
print(nome.count ('i') , "\n")


#RETORNA true (verdadeiro) OU false (falso) PARA UM TESTE se A STRING TERMINA COM UMA STRING ESPECIFICA.
nome = "RafaelMagalhaes@gmail.com"
print(nome.endswith ('gmail.com') , "\n")

#ENCONTRA A POSIÇÃO DO TERMO PROCURADO. LEMBRE-SE COMEÇA POR zero 
nome = "RafaelMagalhaes@gmail.com"
print(nome.find ('@') , "\n")


#VERIFICA SE O TEXTO É todo FEITO COM LETRAS.
nome = "Rafael"
print(nome.isalpha(),"\n")


#VERIFICA SE O TEXTO É FEITO COM NUMEROS
nome = "123"
print(nome.isnumeric(),"\n")


#SUBSTITUI UM CARACTERE ESCOLHIDO POR OUTRO.
nome = "Rafael"
print(nome.replace('a','u'),"\n")


#SEPARA O TEXTO string BASEADO EM ALGUM CARACTERE INDICADO
nome = "Rafael @ Ana Beatriz"
print(nome.split('@'),"\n")


#COLOCA TODAS AS LETRAS INICIAIS EM MAIUSCULAS
nome = "Rafael de Almeida de Magalhaes"
print (nome.title(),"\n")


#RETIRA OS CARACTERES INDESEJDADOS, COMO POR EXEMPLO ESPAÇOS QUE NAO AGRAGAM VALOR
nome = " rafael de almeida de magalhaes "
print(nome.strip(),"\n")


#RETORNA true OU false PARA UM TESTE DE UMA STRING SE INICIA COM UM TEXTO ESPECIFICO.
nome = "rafael 2008"
print(nome.startswith("raf"),"\n")
print(nome.startswith("Raf"),"\n")


