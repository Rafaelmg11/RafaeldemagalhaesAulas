pessoas_presentes = ['John Snow','Jessie Pinkman','Aria Stark','Tyrion Lannister']

#QUERO SABER SE UMA PESSOA ESPECIFICA ESTÁ PRESENTE

chamada = 'Aria Stark'

for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} está presente".format(chamada))
        break
    else:
        print('Só um print para monstrar que ja passou por essa pessoa: '+str(pessoa))





pessoas_presentes = ['John Snow','Jessie Pinkman','Aria Stark','Tyrion Lannister']

#QUERO SABER SE UMA PESSOA ESPECIFICA ESTÁ PRESENTE

chamada = 'Aria Stark'

for pessoa in pessoas_presentes:
    if pessoa == chamada:
        print("{} está presente".format(chamada))
        break
    else:
        print('Só um print para monstrar que ja passou por essa pessoa: '+str(pessoa))
        continue
        print("Só para monstrar que não vai ser printado")