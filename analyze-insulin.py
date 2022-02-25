# Exercice lab 10
import re

# Ouvrir le ficher preproinsulin_seq.txt en lecture
newFile = open ('preproinsulin_seq.txt', 'r')
# On recupère le contenu du fichier
preoinsulin = newFile.read()
""" Methode 1
# Supprimer les caractères ORIGIN, 1 , 61 , // , les espaces et les chariots de retour
x = ''.join(filter(str.isalnum, preoinsulin))
y = re.sub("ORIGIN","",x)
z = re.sub('\d','',y) 
""" 

""" Methode 2 """
# r'':pour indiquer regex, \d{1,2} indique le nombre à 1 et 2 chiffre, \s pour les espaces, le slash et antislash x2 inquide les //
z = re.sub(r'\d{1,2}|ORIGIN|\s|\/\/', "", preoinsulin)
print(z)
# ouvrir le fichier preproinsulin_seq_clean.txt en ecriture
file = open('preproinsulin_seq_clean.txt', 'w')
file.write(z)
# on ferme le fichiers newFile et file
newFile.close()
file.close()
# le nombre de caractères contenu dans le fichier
print(len(z))

# extraire les caractères 1 à 24
zn = z[0:25]
print(zn)
print(zn)
#écriture sur le fichier
fileIsinsulin = open ('lsinsulin-seq-clean.txt','w')
fileIsinsulin.write(zn)
fileIsinsulin.close()
#extraire les caratères 25-54 et écrire sur le fichier binsulin
bn = z[24:54]
print(bn)
print(len(bn))
bInsulin = open ('binsulin-seq-clean.txt','w')
bInsulin.write(bn)
bInsulin.close()
#extraire les caratères 55-89 et écrire sur le fichier cinsulin
cn = z[54:89]
print(cn)
print(len(cn))
cInsulin = open ('cinsulin-seq-clean.txt','w')
cInsulin.write(cn)
cInsulin.close()
#extraire les caratères 90-110 et écrire sur le fichier ainsulin
an = z[89:110]
print(an)
print(len(an))
aInsulin = open ('ainsulin-seq-clean.txt','w')
aInsulin.write(an)
aInsulin.close()
