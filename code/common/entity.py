import vector
from tkinter import *

class Entity:
    def __init__(pos):
        self.pos = pos

    #Copy les changements d'état de l'entité venant du server
    def server_update():
        pass

    #Calcule les changements d'état de l'entité
    def update():
        pass

    #Affiche l'entité
    def draw():
        pass
