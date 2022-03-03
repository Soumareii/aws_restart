import math

# Afficher les nombres premier de 1 à 250
num = 1
primeNumber = []
mod = 0
while num <= 250:
    for div in range(2,num):
        if num%div == 0:
           break
    else:
        primeNumber.append(num)
    num+=1
print(primeNumber,'\n')
r = str(primeNumber)
result = open('results.txt', 'w')
result.write(r)
result.close()
print("Affichage du fichier results.txt\n")

print(open('results.txt','r').read())
