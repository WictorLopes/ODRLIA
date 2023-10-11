#The line below is to run in Brazil
# -*- coding: utf-8 -*-
##----- Importation des Modules -----##
from tkinter import *
##----- Variables globales -----##
# Coordonn�es X,Y des 5 anneaux :
coord = [[20,30], [120,30], [220, 30], [70,80], [170,80]]
# Couleurs des 5 anneaux :
coul = ["red", "yellow", "blue", "green", "black"]
##----- D�finition des Fonctions -----##
##----- Cr�ation de la fen�tre -----##
fen = Tk()
fen.title('BU�s lifecycle of customer-file')
##----- Cr�ation des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)
##----- Cr�ation du canevas -----##
dessin = Canvas(fen, width =550, height =300, bg ="ivory")
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)
##----- Objets graphiques -----##
# Dessin des 5 anneaux :


dessin.create_oval(20, 30, 20+50, 30 +50, width =3, outline ="black")
dessin.create_text(20 + 23, 30 + 23, text="created")
dessin.create_oval(20, 150, 20+50, 150 +50, width =3, outline ="black")
dessin.create_text(20 + 23, 150 + 23, text="opened")
dessin.create_line(45, 80, 45, 150, arrow='last')


dessin.create_oval(150, 30, 150+50, 30 +50, width =3, outline ="black")
dessin.create_text(150 + 23, 30 + 23, text="archived")
dessin.create_oval(150, 150, 150+50, 150 +50, width =3, outline ="black")
dessin.create_text(150 + 23, 150 + 23, text="closed")
dessin.create_line(175, 80, 175, 150, arrow='last')

dessin.create_oval(280, 30, 280+50, 30 +50, width =3, outline ="black")
dessin.create_text(280 + 23, 30 + 23, text="verified")
dessin.create_oval(280, 150, 280+50, 150 +50, width =3, outline ="black")
dessin.create_text(280 + 23, 150 + 23, text="rejected")
dessin.create_line(300, 80, 300, 150, arrow='last')


dessin.create_oval(340, 150, 340+50, 150 +50, width =3, outline ="black")
dessin.create_text(340 + 23, 150 + 23, text="accept")
dessin.create_line(300, 80, 360, 150, arrow='last')

dessin.create_oval(480, 150, 480+50, 150 +50, width =3, outline ="black")
dessin.create_text(480 + 23, 150 + 23, text="update")

##----- Programme principal -----##
fen.mainloop()# Boucle d'attente des �v�nements