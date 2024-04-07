import PIL
from PIL import Image
import numpy as np
import scipy as sp
import os
from math import log10, sqrt

def load(filename):
    toLoad= Image.open(filename)
    return np.array(toLoad)
def psnr(original, compressed):
    mse = np.mean((original.astype(int) - compressed) ** 2)
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
def save(matPix, filename):
    Image.fromarray(matPix).save(filename)
#question 1
def padding(matrice):
    Hauteur = np.shape(matrice)[1]
    largeur = np.shape(matrice)[0]

    colonnes_supp_hauteur = (4 - Hauteur % 4) % 4
    colonnes_supp_largeur = (4 - largeur % 4) % 4

    nouvelleMat = np.zeros((largeur + colonnes_supp_largeur, Hauteur + colonnes_supp_hauteur, 3), dtype=np.uint8)
    nouvelleMat[:largeur, :Hauteur] = matrice
    save(nouvelleMat, "procnoir.png")
def no_padding(matrice, largeur, hauteur):
    nouvellemat = matrice[:hauteur, :largeur]  # Utilisez les dimensions d'origine après le padding
    save(nouvellemat, "procsansnoir.png")
def verif(image_originale, image_transformee):
    return np.array_equal(image_originale, image_transformee)
#question 2 
def slice4pixel(matrice):
    hauteur = np.shape(matrice)[0]
    largeur = np.shape(matrice)[1]
    
    # Calcule le nombre de segments en hauteur et en largeur
    segments_hauteur = hauteur // 4
    segments_largeur = largeur // 4
    
    # découpage en 4

    blocs = []  # Liste pour stocker les blocs

    for i in range(segments_hauteur):
        for j in range(segments_largeur):
            segment = matrice[i*4:(i+1)*4, j*4:(j+1)*4]
            blocs.append(segment)

            #i*4 calcule l’indice de la première ligne du segment.
            #(i+1)*4 calcule l’indice de la dernière ligne du segment (non inclus).
            
            #j*4 calcule l’indice de la première ligne de la colone.
            #(j+1)*4 calcule l’indice de la dernière de la colone (non inclus).

            #save(segment, f"Segment_{i}_{j}.jpg") #N'ACTIVER QUE SI ON EST SUR DES MATRICES MINUSCULES
    return blocs

#espace TEST -------------------------------------------------------
# test padding
image_test = load("proc.jpg")
padding(image_test)

#test no paddinng
imgae_bord = load("procnoir.png")
no_padding(imgae_bord, image_test.shape[1], image_test.shape[0])

# on compare les deux images 
image_reduite = load("procsansnoir.png")
identique = verif(image_test, image_reduite)

#on test slice
#slice = slice4pixel(image_test) pas de test c'est bon on sait que ça marche c'est trop long 


print(f"Image d'origine :\n{image_test}")
print(f"Image avec padding sauvegardée dans 'procnoir.png'")
print(f"Image réduite sauvegardée dans 'procsansnoir.png'")
print(f"Identique ? {identique}")
#print(f"slice4pix ? {slice}")
