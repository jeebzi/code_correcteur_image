from random import *
import sys
import itertools

def splitbytes(x):
	return [(x >> 4) & 15 , x & 15]


def code(m):
# ici on sait qu'en entree on n'aura a traiter
# que des mots de 4 bits
	mot = 0
	j = 3
	while  (j >= 0):
		if (m & (1 << j)):
			mot = mot ^ G[3-j]
		j=j-1
	return(mot)

# Matrice de Hamming, la dÃ©composition en base 2 
# de chacun de ces entiers correspond Ã  une ligne 
# de la matrice gÃ©nÃ©ratrice 

G=[75,42,25,7]

source = open(sys.argv[1], "r")
destination = open("enc_"+sys.argv[1], "w")
#lecture en tÃªte
laligne = source.readline()
destination.write(laligne)
#lecture taille
laligne = source.readline()
destination.write(laligne)
#lecture niveau max de gris
laligne = source.readline()
destination.write(laligne)
for laligne in source:
	sequence = list(map(int,laligne.rstrip('\n\r').split()))
	sequence = list(map(splitbytes,sequence))
	# pour supprimer les sous-listes 
	sequence = list(itertools.chain(*sequence))
	# etape de codage 
	sequence = list(map(str,map(code,sequence)))
	sequence = ' '.join(sequence)
	destination.write(sequence+'\n')
source.close()
destination.close()

