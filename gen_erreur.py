from encode import read_pgm
import sys
import random as rd

def generer_erreur(mot, n):
    """
    génère une erreure sur un mot de n bit
    le primer bit et le bit de poid faible
    """
    indice_erreur = rd.randint(0, n - 1)
    mot_bruite = mot ^ (1 << indice_erreur)
    return mot_bruite

def bruite_image(image, n):
    """
    bruite une image avec ces mot codée sur n bits
    """
    image_bruite = []
    i = 0
    while i < len(image):
        mot = image[i]
        mot_bruite = generer_erreur(mot, n)
        image_bruite += [mot_bruite]
        i += 1
    return image_bruite

def write_image(dst, src, image):
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
    while i < len(image):
        if cpt >= 30:
            f.write("\n")
            cpt = 0
        f.write(str(image[i])+" ")
        i += 1
        cpt += 1
    f.close()

if __name__ == "__main__":
    image_encode = read_pgm(sys.argv[1])
    image_bruite = bruite_image(image_encode, 7)
    write_image("err_"+sys.argv[1], sys.argv[1], image_bruite)
