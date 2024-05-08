from PIL import Image as img, ImageTk as imgtk
from tkinter import *

#Stocke les chemins des images du programme
stored_img_path=[]
#Stocke les images du programme
stored_img=[]

'''
Ajout d'image au canvas.
Pour garder les images en mémoire, on let met dans une variable global.
Afin d'éviter la surcharge d'image, on mentient en mémoire leur chemin de fichier pour ne pas mettre en mémoire plus d'une fois.
'''
def createIMG(canv, filepath, x, y):
    if filepath not in stored_img_path:
        with img.open(filepath) as PIL_img:
            stored_img_path.append(filepath)
            stored_img.append(imgtk.PhotoImage(PIL_img))
            img_id = canv.create_image(x,y,image=stored_img[len(stored_img)-1])
    else:
        img_id = canv.create_image(x,y,image=stored_img[stored_img_path.index(filepath)])
    return img_id
