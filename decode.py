import sys
from encode import read_pgm
from gen_erreur import write_image

def decode(image_encode, n, k):
    """
    décode l'image de mot de taille n en mot de taille k
    """
    i = 0
    image = []
    while i < len(image_encode) - 1:
        code_fort = image_encode[i]
        code_faible = image_encode[i + 1]
        poid_fort = code_fort >> (n - k)
        poid_faible = code_faible >> (n - k)
        mot = (poid_fort << k) + poid_faible
        image += [mot]
        i += 2
    return image

if __name__ == "__main__":
    image_encode = read_pgm(sys.argv[1])
    image = decode(image_encode, 7, 4)
    print(len(image))
    write_image("image_corrige.pnm", sys.argv[1], image)
