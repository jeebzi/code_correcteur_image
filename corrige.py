from encode import read_pgm, encode_mot
import sys
from gen_erreur import write_image

matrice_controle = [1, 2, 3, 4, 5, 6, 7]

def corrige_erreur(image_bruite, n):
    image_corrige = []
    i = 0
    while i < len(image_bruite):
        code_bruite = image_bruite[i]
        syndrome = encode_mot(code_bruite, matrice_controle, n)
        code_corrige = code_bruite ^ (1 << n - syndrome)
        image_corrige += [code_corrige]
        i += 1
    return image_corrige

if __name__ == "__main__":
    image_bruite = read_pgm(sys.argv[1])
    image_corrige = corrige_erreur(image_bruite, 7)
    write_image("corr_"+sys.argv[1], sys.argv[1], image_corrige)

