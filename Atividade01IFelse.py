#Faça um programa que o ususario digite um número e diga se o numero é superior a 20,inferior a 10 ou se esta entre 10 e 20
num = int (input("Digite um numero qualquer: "))

if num > 20:
    print("O número digitado é superior a 20")
else:
    if num < 10:
        print("O número digitado é inferior a 10")
    else:
        print ("O número digitado esta entre 10 e 20")
