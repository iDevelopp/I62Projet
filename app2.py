import tkinter as tk

# Positions des éléments de l'interface

CANV_X = 0
CANV_Y = 0
CANV_WIDTH = 1200
CANV_HEIGHT = 800

FRM_X = 220
FRM_Y = 65
FRM_WIDTH = 800
FRM_HEIGHT = 500

MODE_TXT_X = 600
MODE_TXT_Y = 240

BTN_CLIENT_X = 360
BTN_CLIENT_Y = 330
BTN_CLIENT_WIDTH = 80
BTN_CLIENT_HEIGHT = 40

BTN_SERVER_X = 540
BTN_SERVER_Y = 330
BTN_SERVER_WIDTH = 80
BTN_SERVER_HEIGHT = 40

BTN_SEPARATE_X = 720
BTN_SEPARATE_Y = 330
BTN_SEPARATE_WIDTH = 80
BTN_SEPARATE_HEIGHT = 40

BTN_STOP_X = 60
BTN_STOP_Y = 680
BTN_STOP_WIDTH = 80
BTN_STOP_HEIGHT = 40

# Methodes

"""
def start_client_view(event=None):
"""

# Fenêtre principale

root = tk.Tk()
root.geometry("1200x800")

canv = tk.Canvas(root, bg="white")
canv.place(x = CANV_X, y = CANV_Y, width = CANV_WIDTH, height = CANV_HEIGHT)

"""
frm = tk.Frame(root, bg='green')
frm.place(x = FRM_X, y = FRM_Y, width = FRM_WIDTH, height = FRM_HEIGHT)
"""

# Choix du mode de simulation entre client, serveur et vue séparée

mode_st = "Choisir un mode de simulation."
mode_txt = canv.create_text(MODE_TXT_X, MODE_TXT_Y, fill="black", text=mode_st, font=('Arial', 20))

btn_client = tk.Button(canv, text="CLIENT", bg='black', fg='white')
btn_client.place(x = BTN_CLIENT_X, y = BTN_CLIENT_Y, width = BTN_CLIENT_WIDTH, height = BTN_CLIENT_HEIGHT)
#btn_client.bind('<Button-1>', start_client_view)

btn_server = tk.Button(canv, text="SERVER", bg='black', fg='white')
btn_server.place(x = BTN_SERVER_X, y = BTN_SERVER_Y, width = BTN_SERVER_WIDTH, height = BTN_SERVER_HEIGHT)

btn_separate = tk.Button(canv, text="SEPAREE", bg='black', fg='white')
btn_separate.place(x = BTN_SEPARATE_X, y = BTN_SEPARATE_Y, width = BTN_SEPARATE_WIDTH, height = BTN_SEPARATE_HEIGHT)

"""
btn_stop = tk.Button(canv, text="STOP", bg='black', fg='white')
btn_stop.place(x = BTN_STOP_X, y = BTN_STOP_Y, width = BTN_STOP_WIDTH, height = BTN_STOP_HEIGHT)
"""

# Boucle d'appel

tk.mainloop()
