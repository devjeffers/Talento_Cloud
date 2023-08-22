#Precisamos imprimir um número para cada andar de um hotel de 20 andares. 
#Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos 
#de laços de repetição aprendidos.

#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

#Primeira forma:
for andar in range(1, 21):
    if andar != 13:
        print("Este é o Andar:", andar,"º");

#Segunda Maneira:
andar = 1
while andar <=20:
    if andar !=13:
        print("Este é o Andar:", andar,"º");
    andar += 1;

#Terceira Forma:
for andar in range(21):
    if (andar == 13):
        continue;
    if (andar == 21):
        break
    print("Este é o Andar:", andar, "º");

#Quarta Maneira:
import random
andar = random.randint(1, 21)
while(andar != 13):
    print("Este é o Andar:", andar, "º")
    andar = random.randint(1, 21);

#E quinta Forma:
for andar in range(21, 0, -1):
    if (andar != 13):
       print("Este é o Andar:", andar, "º")
    andar -= 1