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
    """
    Ajoute du remplissage (padding) noir à une image pour garantir que ses dimensions soient des multiples de 4.

    Args:
        matrice (ndarray): Matrice représentant l'image à laquelle ajouter le padding.

    Returns:
        ndarray: Matrice de l'image avec padding.
    """
    # Récupérer les dimensions de l'image
    Hauteur = np.shape(matrice)[1]
    largeur = np.shape(matrice)[0]

    # Calculer le nombre de colonnes de padding nécessaires pour atteindre une dimension multiple de 4
    colonnes_supp_hauteur = (4 - Hauteur % 4) % 4
    colonnes_supp_largeur = (4 - largeur % 4) % 4

    # Créer une nouvelle matrice avec les dimensions ajustées et remplie de pixels noirs
    nouvelleMat = np.zeros((largeur + colonnes_supp_largeur, Hauteur + colonnes_supp_hauteur, 3), dtype=np.uint8)
    nouvelleMat[:largeur, :Hauteur] = matrice

    # Enregistrer l'image avec padding
    save(nouvelleMat, "procnoir.png")

    return nouvelleMat


#verification de la question 1 

def no_padding(matrice, largeur, hauteur):
    """
    Supprime le padding ajouté précédemment à une image, en fonction de ses dimensions d'origine.

    Args:
        matrice (ndarray): Matrice représentant l'image avec padding.
        largeur (int): Largeur originale de l'image avant le padding.
        hauteur (int): Hauteur originale de l'image avant le padding.

    Returns:
        ndarray: Matrice de l'image sans padding.
    """
    # Extraire la partie de l'image correspondant aux dimensions d'origine après le padding
    nouvellemat = matrice[:hauteur, :largeur]

    # Enregistrer l'image sans padding
    save(nouvellemat, "procsansnoir.png")


def verif(image_originale, image_transformee):
    """
    Vérifie si deux images sont identiques.

    Args:
        image_originale (ndarray): Matrice représentant l'image d'origine.
        image_transformee (ndarray): Matrice représentant l'image transformée.

    Returns:
        bool: True si les deux images sont identiques, False sinon.
    """
    return np.array_equal(image_originale, image_transformee)


#Question 2 
def decouper_en_blocs(matrix):
    """
    Découpe une matrice en blocs 4x4 et les stocke dans une liste.
    
    Args:
        matrix (ndarray): Matrice à découper en blocs 4x4.
        
    Returns:
        list: Liste des blocs 4x4.
    """
    blocs = []  #bloc final
    
    # Récupérer les dimensions de la matrice
    hauteur, largeur, canaux = matrix.shape #canaux pour la couleur, en previsions
    
    # Parcourir la matrice en itérant sur les blocs de taille 4x4
    for i in range(0, hauteur, 4):
        for j in range(0, largeur, 4):
            # Extraire le bloc 4x4 à partir de la matrice
            bloc = matrix[i:i+4, j:j+4, :]
            blocs.append(bloc)  
            
    return blocs  

#Question 3
def reconstruire_image(blocs, img_originale):
    """
    Reconstruit une image à partir d'une liste de blocs 4x4.
    
    Args:
        blocs (list): Liste de blocs 4x4.
        img_originale (ndarray): Image originale à partir de laquelle les blocs ont été extraits.
        
    Returns:
        ndarray: Image reconstruite.
    """

    # Récupérer les dimensions de l'image originale
    hauteur, largeur, canaux = img_originale.shape
    
    # Créer une image vide avec les mêmes dimensions que l'image originale
    image_reconstruite = np.zeros((hauteur, largeur, canaux), dtype=np.uint8)
    
    index = 0  # Initialise l'indice pour accéder aux blocs
    # Parcourir l'image en itérant sur les blocs de taille 4x4
    for i in range(0, hauteur, 4):
        for j in range(0, largeur, 4):
            # Remplacer la section correspondante de l'image reconstruite par le bloc actuel
            image_reconstruite[i:i+4, j:j+4, :] = blocs[index]
            index += 1  # Passer au prochain bloc

    #save l'image reconstruite
    save(image_reconstruite, "imereconstruite.png")
    
    return image_reconstruite  


#espace TEST -------------------------------------------------------

print("------------------Session debug------------------")

image_test = load("proc.jpg")#ne pas utiliser celle la directement, pas multiple de 4
padding(image_test) #question 1 

#test question 1 ----------------
imgae_bord = load("procnoir.png")
no_padding(imgae_bord, image_test.shape[1], image_test.shape[0])

# on compare les deux images 
image_reduite = load("procsansnoir.png")
identique = verif(image_test, image_reduite)

#test question 2/3 ----------------
#on décope l'image en bloc de 4
imgdecoup = decouper_en_blocs(imgae_bord)
#on la réassemble
imereconstruite = reconstruire_image(imgdecoup,imgae_bord)


#print(f"Image d'origine :\n{image_test}") afficher la matrice d'origine
print(f"Image avec padding sauvegardée sous le nom 'procnoir.png'")
print(f"Image réduite sauvegardée sous le nom 'procsansnoir.png'")
print(f"Test question 1 fonctionne :  {identique}")
print(f"Test question 2 et 3 fonctionne :  {np.array_equal(imereconstruite, imgae_bord)}")
