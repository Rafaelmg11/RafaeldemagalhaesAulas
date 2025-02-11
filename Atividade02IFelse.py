#Faça um programa que receba uma nota do aluno e se fr superior ou igual a 7 (sete) apareça a mensaguem que ele esta aprovado, se for inferior a 5(cinco) ele esta 
# "não reprovado/reprovado direto " e se estiver entre 5 e 7 apareça mensagem "Não aprovado/Recuperação"

nota = float (input("Digite a nota do aluno: "))
if nota >= 7:
    print("Aprovado!")
else: 
    if nota >= 5:
        print("Não Aprovado/Recuperação")
    else:
        print("Não Aprovado/Reprovado direto")