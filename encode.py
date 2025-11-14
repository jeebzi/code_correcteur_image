#prend un fichier pgm en argument et l'encode en utilisant le code de Hamming
import sys

def read_pgm(chemin):
    """
    lit le fichier pgm et renvoie la matrice des valeurs
    """
    matrice = []
    f = open(chemin, "r")
    f.seek(3)
    for ligne in f:
        liste = list(map(int, ligne.split()))
        matrice += [liste]
    f.close()
    return matrice

def decoupe_octet(matrice):
    """
    prend la matrice de nombre représenté par 8 bits et retourne la matrice de nombre
    représenté par 4 bit
    """
    res = [] #matrice résultat
    i = 0
    while i < len(matrice):
        ligne = []
        j = 0
        while j < len(matrice[i]):
            poid_faible = matrice[i][j] & 15
            poid_fort = (matrice[i][j] >> 4) & 15
            ligne += [poid_fort, poid_faible]
            j += 1
        res += [ligne]
        i += 1
    return res

def encode(mot, matrice_gen):
    """
    encode un mot par la matrice
    """
    pass


if __name__ == "__main__":
    matrice_pixel = read_pgm(sys.argv[1])
    mat = decoupe_octet(matrice_pixel)
    print(mat)
