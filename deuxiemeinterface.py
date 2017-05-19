# -*-coding:Latin-1 -*
'''
    File name: deuxiemeinterface.py
    Author: Roman Devuyst
    Date created: 16/03/2017
    Date last modified: 17/05/2017
    Python Version: 2.7
    Purpose: This file contains the graphic interface of the game Puissance4
'''
#Graphic modules importation
from Tkinter import *
import ttk

#Game intelligence importation
import p4_rsc as motor

######################Contstants##############################
#Game dimensions
WDTH = 700
HGTH = 700
NB_COL = 7
NB_ROW = 6

#Frames dimensions
WDTH_F1 = WDTH 									
HGTH_F1 = HGTH - (HGTH / (NB_ROW + 1))			# Height is number of game rows / total number of rows (NB_ROW + 1)
WDTH_F2 = WDTH
HGTH_F2 = HGTH - NB_ROW*(HGTH / (NB_ROW + 1))	# Height is remainder (last row)

#Columns dimensions
WDTH_COL = WDTH_F1 / NB_COL
HGTH_COL = HGTH_F1

#Player's color
PLAYER_COLOR = ['red','yellow']
##############################################################

#Global variables
current_player = 0
done = 0


#Begin code

#Root window of the interface
root = Tk()

#Content root Frame for all subsequent widgets
content = ttk.Frame(root)
content.pack(side=LEFT, expand = 1)


#################### Main Frames ###############################

#Board Frame
frame1 = ttk.Frame(content, width = WDTH_F1, height = HGTH_F1) 
#Information Frame
frame2 = ttk.Frame(content, width = WDTH_F2, height = HGTH_F2) 

frame1.pack(expand = 1)
frame2.pack(expand = 1)


################ Upper Frame Widgets Definition ##################

######## Canvas as columns for frame1 #####

#Recipient for the canvas references
columns = []

#Initialisation loop
for i in range(NB_COL):
	columns.append(Canvas(frame1, width = WDTH_COL, height = HGTH_COL, background = "blue", highlightthickness=0)) 
	columns[i].grid(column = i, row = 0)
	

###################### Draw the circles ##########################

#Space between column border and the circle
offset = WDTH_COL / 20

#Virtual height of a board square
HGTH_CASE = HGTH_COL / NB_ROW
 
# Initialisation of the circles in a list of lists (2 dimensions array with dimensions corresponding to the game board)
# create_oval : 1st arg is distance from left side of the column
#				2nd arg is distance from upper side of the virtual square
#				3rd arg is distance from right side of the column
#				4th arg is distance from lower side of the column
columns_grid = [ [ columns[j].create_oval(offset, i*HGTH_CASE + offset,
				 WDTH_COL - offset, (i + 1)*HGTH_CASE - offset, fill = 'white') for j in range(NB_COL) ]
			 for i in range(NB_ROW)]

################ Lower Frame Widgets Definition ##################

#Canvas with same dimension than the frame to fill it with a color
canvas1 = Canvas(frame2, width = WDTH, height = HGTH_F2, background = "white", highlightthickness=0)
canvas1.grid(column = 0, row = 0, columnspan = 7)

######Current player displayer #######
#First a label
joueur = Label(frame2, text = "Joueur:", background = "white")
joueur.grid(column = 0, row = 0)

#Then a circle (color updated at each move)
player_circle  = canvas1.create_oval(WDTH_COL - WDTH_COL/10, HGTH_F2/2 - HGTH_F2/10, WDTH_COL + WDTH_COL/10,
 HGTH_F2/2 + HGTH_F2/10, fill = PLAYER_COLOR[current_player])

######## Winner Displayer ########

#Variable containing the winning message, initially empty
text = StringVar()
#Displayed in a Label
winner = Label(frame2, textvariable = text, background = "white")
winner.grid(column = 1, row = 0, columnspan = 3)


###### Mode choice scrollbar ###### NOTE : Not used
variable = StringVar(frame2)
variable.set("2 Joueurs") # default value
mode = OptionMenu(frame2, variable, "1 Joueur", "2 Joueurs")
mode.grid(column = 4, row = 0)

################## Methods definition and Widgets Binding ###################
 
def reset_game():
	""" Method which resets the current_player to 0, and the grid's circles to default color
		Calls motors's reset function to do the same actions in the resources
 	"""
	global current_player
	global done
	for i in range(NB_ROW):
		for j in range(NB_COL):
			columns[j].itemconfig(columns_grid[i][j], fill = "white")

	motor.reset()
	current_player = 0
	canvas1.itemconfig(player_circle, fill = PLAYER_COLOR[current_player])
	done = 0

def changecolor(canvas, player, row):
	""" Method which changes the color of the circle in the "canvas"th column and the "row"th row to he "player"'s color'
 	"""
	canvas.itemconfig(columns_grid[row][0], fill = PLAYER_COLOR[player])
	canvas1.itemconfig(player_circle, fill = PLAYER_COLOR[(player + 1) % 2])


def event_player(event):
	""" Method called uppon a player's click on a game column
		if game is finished, does nothing
		else checks validity of the move using motor's method
		if the move is valid, colors the corresponding circle and update current_player
 	"""
	global current_player
	global done
	if not done :
		column = event.widget.winfo_x()/WDTH_COL 	#winfo_x returns the upper left x coordinate relative to the upper 
		ligne, goodMove = motor.playMove(column)
	
		if goodMove:								#left corner of its parent
			changecolor(event.widget, current_player, ligne)
			if motor.checkWinner(ligne, column):
				done = 1
				winner = "Le joueur " + str(current_player) +" a gagne !"
				text.set(winner)
			current_player = (current_player + 1) % 2


#Binds click event to each column with defined above method
for i in range(NB_COL):
	columns[i].bind("<Button-1>", event_player)

#Creating "Quitter" Button with the defined quit method
quit = Button(frame2, text="Quitter", command = quit)
quit.grid(column = 6, row = 0)

#Creating "Rejouer" Button with the defined above method
replay = Button(frame2, text = "Rejouer", command = reset_game)
replay.grid(column = 5, row = 0)

# Displays the main window in an infinite loop
root.mainloop()