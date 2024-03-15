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
    
def slice4part(matrice):
    Hauteur= np.shape(matrice)[1]
    largeur= np.shape(matrice)[0]
    print(largeur/2)
    A1 = matrice[:largeur//2 , :Hauteur//2]
    A2 = matrice[largeur//2: , :Hauteur//2]
    A3 = matrice[:largeur//2 , Hauteur//2 :]
    A4 = matrice[ largeur//2 : , Hauteur//2 :]
    
    save(A1, "A1.jpg")
    save(A2, "A2.jpg")
    save(A3, "A3.jpg")
    save(A4, "A4.jpg")



HauteurBase= np.shape(load("proc.jpg"))[1]
largeurBase= np.shape(load("proc.jpg"))[0]

   
padding(load("proc.jpg"))
no_padding(load("procnoir.jpg"),largeurBase, HauteurBase)
slice4part(load("procnoir.jpg"))
changed(load("proc.jpg"), load("sansNoir.jpg"))
   

