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
        matrice += liste
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
        poid_faible = matrice[i] & 15
        poid_fort = (matrice[i] >> 4) & 15
        res += [poid_fort, poid_faible]
        i += 1
    return res

def encode(mot, matrice_gen, k, n):
    """
    encode un mot de taille k par la matrice de dimsension n x k
    """
    code = 0
    i = 0
    while i < n:
        j = 0
        b = 0 # 0 ou 1
        while j < k:
            b = b ^ (((mot >> ( k - j + 1)) & 1) & ((matice_gen[j] >> (n - i + 1)) & 1)) 
            j += 1
        code += (b << (n - i + 1))
    return code

matrice_gen_hamming = [70, 37, 19, 15]
matrice_parite_hamming = [85, 51, 15]


if __name__ == "__main__":
    matrice_pixel = read_pgm(sys.argv[1])
    mat = decoupe_octet(matrice_pixel)
    print(mat)
