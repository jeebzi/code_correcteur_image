#prend un fichier pgm en argument et l'encode en utilisant le code de Hamming
import sys

def read_pgm(chemin):
    """
    lit le fichier pgm et renvoie la matrice des valeurs
    """
    matrice = []
    f = open(chemin, "r")
    for _ in range(3):
        f.readline()
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

def encode_mot(mot, matrice_gen, k):
    """
    encode un mot de taille k par la matrice de dimension n x k en binaire
    """
    code = 0
    i = 0
    while i < k:
        if (mot >> (k - i - 1)) & 1:
            code = code ^ matrice_gen[i]
        i += 1
    return code

def encode_image(image, matrice_gen, k):
    """
    encode toute l'image grâce à la matrice génératrice, la taille en binaire des mots est k
    """
    image_encode = []
    i = 0
    while i < len(image):
        mot = image[i]
        code = encode_mot(mot, matrice_gen, k)
        image_encode += [code]
        i += 1
    return image_encode

matrice_gen_hamming = [67, 37, 22, 15]
# G=[75,42,25,7]
matrice_parite_hamming = [4, 2, 6, 1, 3, 7]

def write_image_encode(dst, src, image_encode):
    f=open(src, "r")
    entete = []
    for _ in range(3):
        entete += [f.readline()]
    f.close()

    f = open(dst, "w")
    for ligne in entete:
        f.write(ligne)

    i = 0
    cpt = 0
    while i < len(image_encode):
        if cpt >= 30:
            f.write("\n")
            cpt = 0
        f.write(str(image_encode[i])+" ")
        i += 1
        cpt += 1
    f.close()



if __name__ == "__main__":
    image = read_pgm(sys.argv[1])
    print(len(image))
    image_coupe = decoupe_octet(image)
    image_encode = encode_image(image_coupe, matrice_gen_hamming, 4)
    write_image_encode("enc_"+sys.argv[1], sys.argv[1], image_encode)
