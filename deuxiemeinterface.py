
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
	columns.append(Canvas(frame1, width = WDTH_COL, height = HGTH_COL, background = "blue")) #TODO: COLOR CONSTANT
	columns[i].grid(column = i, row = 0)
	

#Draw the circles
offset = WDTH_COL / 20
HGTH_CASE = HGTH_COL / NB_ROW

columns_grid = [ [ columns[j].create_oval(offset, i*HGTH_CASE + offset,
				 WDTH_COL - offset, (i + 1)*HGTH_CASE - offset, fill = 'white') for j in range(NB_COL) ]
			 for i in range(NB_ROW)]



def changecolor(canvas, player, row):
	canvas.itemconfig(columns_grid[row][0], fill = PLAYER_COLOR[player])




def event_player(event):

	column = event.widget.winfo_x()/WDTH_COL #winfo_x returns the upper left x coordinate relative to the upper 
	ligne, goodMove = motor.playMove(column)
	global current_player
	print 
	if goodMove:								#left corner of its parent
		changecolor(event.widget, current_player, ligne)
		current_player = (current_player + 1) % 2

for i in range(NB_COL):
	columns[i].bind("<Button-1>", event_player)







root.mainloop()