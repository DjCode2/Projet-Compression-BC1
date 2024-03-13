import PIL as pil
from PIL import Image
from PIL import ImageTk 
import numpy as np



matrice = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
print(matrice)
print("")

#sauvegarder image
def save(matPix, filename):
    Image.fromarray(matPix).save(filename)

#charger image
def load(filename):
    return np.array(pil.Image.open(filename))


def question1(matrice):
    longeur= np.shape(matrice)[0]
    largeur= np.shape(matrice)[1]

    colone_supp_longueur = (4 - longeur%4)%4
    colone_supp_largeur = (4 - largeur%4)%4

    nouvelleMat= np.empty((longeur+colone_supp_longueur,largeur+colone_supp_largeur),dtype=np.uint8)
    nouvelleMat[:longeur,:largeur]= matrice

    print(nouvelleMat)

    

   




question1(matrice)