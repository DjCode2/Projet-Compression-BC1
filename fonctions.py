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
    Hauteur= np.shape(matrice)[1]
    largeur= np.shape(matrice)[0]

    colone_supp_Hauteur = (4 - Hauteur%4)%4
    colone_supp_largeur = (4 - largeur%4)%4

    nouvelleMat= np.zeros((largeur+colone_supp_largeur,Hauteur+colone_supp_Hauteur,3),dtype=np.uint8)

    nouvelleMat[:largeur,:Hauteur]= matrice
    save(nouvelleMat, "procnoir.jpg")
    #print(nouvelleMat) #debug

def no_padding(matrice, largeur, hauteur):
    nouvellemat = matrice[:largeur, :hauteur]
    save(nouvellemat, "sansNoir.jpg")
    

def changed(matrice, nouvellematrice):
    # print(matrice[matrice.shape[0]-1,matrice.shape[1]-1])
    # print(matrice[nouvellematrice.shape[0]-1,nouvellematrice.shape[1]-1])
    if np.shape(matrice) == np.shape(nouvellematrice) :
        # if((matrice == nouvellematrice).all()):
            # if np.array_equal(matrice, nouvellematrice):
                return True
    return False

#question 2 
    
def slice4pixel(matrice):
    hauteur = np.shape(matrice)[0]
    largeur = np.shape(matrice)[1]
    
    # Calcule le nombre de segments en hauteur et en largeur
    segments_hauteur = hauteur // 4
    segments_largeur = largeur // 4
    
    # découpage en 4
    for i in range(segments_hauteur):
        for j in range(segments_largeur):
            # Découpe le segment actuel de la matrice
            segment = matrice[i*4:(i+1)*4, j*4:(j+1)*4]
            
            #save(segment, f"Segment_{i}_{j}.jpg") #N'ACTIVER QUE SI ON EST SUR DES MATRICES MINUSCULES


HauteurBase= np.shape(load("proc.jpg"))[1]
largeurBase= np.shape(load("proc.jpg"))[0]

   
padding(load("proc.jpg"))
no_padding(load("procnoir.jpg"),largeurBase, HauteurBase)
slice4pixel(load("procnoir.jpg"))
changed(load("proc.jpg"), load("sansNoir.jpg"))
   



def save(segment, filename):
    # Convertit le segment en image
    image = Image.fromarray(segment)
    # Sauvegarde l'image
    image.save(filename)

# Exemple d'utilisation avec une matrice de test
matrice_test = np.random.randint(0, 255, size=(16, 16))  # Crée une matrice 16x16 avec des valeurs aléatoires entre 0 et 255
slice4pixel(matrice_test)
