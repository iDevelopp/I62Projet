import situation
from tkinter import *

class Sitac:
    def __init__(situation):
        self.situation = situation

    def display():
        for i in range(len(self.situation.OF_units)):
            self.situation.OF_units[i].draw()

if __name__ == "__main__":
    WIN = Tk()
    WIN.geometry("800x600")
    CAN = Canvas(WIN, width="800", height="600")

    situation = Situation(800,600)
    sitac = Sitac(situation)
    situation.add_entity("OF_R", Position(50, 50))
    sitac.display()
