# -*-coding:Latin-1 -*
import Tkinter as tk
from Tkinter import *

fenetre = Tk ()

fenetre.configure(bg = "yellow")


fenetre_name = Label (fenetre, text = "Hello")
fenetre_name.pack()

boutton_Quit = Button (fenetre, text = "quitter la fenetre" , command = fenetre.quit)
boutton_Quit.pack()

boutton_PlusouMoins = Button (fenetre, text = "+/-" )
boutton_PlusouMoins.pack()


boutton_Agrandir_Fenetre = Button(fenetre, text='RESET', font='Arial -20 bold', relief='flat', bg='red', fg = 'blue', activebackground = "blue")
boutton_Agrandir_Fenetre.pack()





fenetre.mainloop ()
