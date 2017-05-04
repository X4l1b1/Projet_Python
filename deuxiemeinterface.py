
from Tkinter import *
import ttk
import p4_rsc as motor

#Game dimensions
WDTH = 700
HGTH = 700
NB_COL = 7
NB_ROW = 6

#Frames dimensions
WDTH_F1 = WDTH
HGTH_F1 = HGTH - (HGTH / (NB_ROW + 1))
WDTH_F2 = WDTH
HGTH_F2 = HGTH - NB_ROW*(HGTH / (NB_ROW + 1))

#Columns dimensions
WDTH_COL = WDTH_F1 / NB_COL
HGTH_COL = HGTH_F1


PLAYER_COLOR = ['red','yellow']

current_player = 0
done = 0

root = Tk()

#Content root Frame
content = ttk.Frame(root)
content.pack(side=LEFT, expand = 1)


#Globale Frames
frame1 = ttk.Frame(content, width = WDTH_F1, height = HGTH_F1)

frame2 = ttk.Frame(content, width = WDTH_F2, height = HGTH_F2)

frame1.pack(expand = 1)
frame2.pack(expand = 1)


#Canvas Columns for frame1
columns = []
for i in range(NB_COL):
	columns.append(Canvas(frame1, width = WDTH_COL, height = HGTH_COL, background = "blue", highlightthickness=0)) 
	#TODO: COLOR CONSTANT
	columns[i].grid(column = i, row = 0)
	

#Draw the circles
offset = WDTH_COL / 20
HGTH_CASE = HGTH_COL / NB_ROW

columns_grid = [ [ columns[j].create_oval(offset, i*HGTH_CASE + offset,
				 WDTH_COL - offset, (i + 1)*HGTH_CASE - offset, fill = 'white') for j in range(NB_COL) ]
			 for i in range(NB_ROW)]

#Lower Frame Widgets Definition
canvas1 = Canvas(frame2, width = WDTH, height = HGTH_F2, background = "white", highlightthickness=0)
canvas1.grid(column = 0, row = 0, columnspan = 7)

#Current player displayer #TODO: OVAL
joueur = Label(frame2, text = "Joueur:", background = "white")
joueur.grid(column = 0, row = 0)
player_circle  = canvas1.create_oval(WDTH_COL - WDTH_COL/10, HGTH_F2/2 - HGTH_F2/10, WDTH_COL + WDTH_COL/10,
 HGTH_F2/2 + HGTH_F2/10, fill = PLAYER_COLOR[current_player])

#Winner Displayer
text = StringVar()
winner = Label(frame2, textvariable = text, background = "white")
winner.grid(column = 1, row = 0, columnspan = 3)


#Mode choice scrollbar
variable = StringVar(frame2)
variable.set("2 Joueurs") # default value
mode = OptionMenu(frame2, variable, "1 Joueur", "2 Joueurs")
mode.grid(column = 4, row = 0)


def reset_game():
	global current_player
	global done
	for i in range(NB_ROW):
		for j in range(NB_COL):
			columns[j].itemconfig(columns_grid[i][j], fill = "white")

	motor.reset()
	current_player = 0
	canvas1.itemconfig(player_circle, fill = PLAYER_COLOR[current_player])
	done = 0

#Quit and replay Buttons
quit = Button(frame2, text="Quitter", command = quit)
replay = Button(frame2, text = "Rejouer", command = reset_game)
quit.grid(column = 6, row = 0)
replay.grid(column = 5, row = 0)

def changecolor(canvas, player, row):
	canvas.itemconfig(columns_grid[row][0], fill = PLAYER_COLOR[player])
	canvas1.itemconfig(player_circle, fill = PLAYER_COLOR[(player + 1) % 2])


def event_player(event):
	global current_player
	global done
	if not done :
		column = event.widget.winfo_x()/WDTH_COL #winfo_x returns the upper left x coordinate relative to the upper 
		ligne, goodMove = motor.playMove(column)
	
		if goodMove:								#left corner of its parent
			changecolor(event.widget, current_player, ligne)
			if motor.checkWinner(ligne, column):
				done = 1
				winner = "Le joueur " + str(current_player) +" a gagne !"
				text.set(winner)
			current_player = (current_player + 1) % 2


#Add click event to each column
for i in range(NB_COL):
	columns[i].bind("<Button-1>", event_player)

root.mainloop()