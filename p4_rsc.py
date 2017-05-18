# -*-coding:Latin-1 -*
'''
    File name: p4_rsc.py
    Author: Roman Devuyst
    Date created: 16/03/2017
    Date last modified: 17/05/2017
    Python Version: 2.7
    Purpose: This file contains the motor functions of the game Puissance4
'''
###################### Contstants and Global Variables ##############################

###### Game dimensions ######
largeur = 7
hauteur = 6

##### Global variables #####
moves = 0
gagnant = -1
currentplayer = 0
symboles = ["X", "O"]

#Initialisation of the game's grid
grille =[ ["-" for x in range (largeur)] for y in range (hauteur)]


def reset():
	""" Method which sets the game's board array to its initial values and the currentplayer to '0'
 	"""
	for x in range (hauteur):
		for y in range(largeur):
			grille[x][y] = "-"
	currentplayer = 0



def playMove(colonne):
	""" Method which, given a column index, checks wether :
				- the index is not out of bounds
				- the column isn't full
		if so, it fills the first valid element of the board with the current player's symbol
		returns anyway the move's row and validity
 	"""
	ligne = -1
	goodMove = False
	for y in range (hauteur):
		if (grille[hauteur -1 - y][colonne] == "-"):
			goodMove = True
			ligne = hauteur -1 -y
			break
		if not goodMove:
					continue
	if goodMove:
		grille [ligne][colonne] = symboles[currentplayer]

	return ligne, goodMove



def checkLigne(ligne,colonne):
	""" Checks wether the given square coordinate's row contains a winning move
		returns the answer
 	"""
	adjacent = 0
	for x in range (3):
		if(colonne + x + 1 < largeur):
			if grille[ligne][colonne + x + 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	for x in range (3):
		if(colonne - x - 1 >= 0):
			if grille[ligne][colonne - x - 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	if adjacent == 3:
		return True
	else:
		return False

def checkColonne(ligne,colonne):
	""" Checks wether the given square coordinate's column contains a winning move
		returns the answer
 	"""
	adjacent = 0
	for x in range (3):
		if(ligne + x + 1 < hauteur):
			if grille[ligne + x + 1][colonne] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	for x in range(3):
		if(ligne - x - 1 >= 0):
			if grille[ligne -x - 1][colonne] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	if adjacent == 3:
		return True
	else:
		return False
				

def checkDiagAsc(ligne,colonne):
	""" Checks wether the given square coordinate's diagonal (from bottom left to top right) contains a winning move
		returns the answer
 	"""
	adjacent = 0 
	for x in range (3):
		if (ligne + x + 1 < hauteur) and (colonne - x - 1 >= 0):
			if grille[ligne + x + 1][colonne - x - 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	for x in range (3):
		if (ligne - x - 1 >= 0) and (colonne + x + 1 < largeur):
			if grille[ligne - x - 1][colonne + x + 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	if adjacent == 3:
		return True
	else:
		return False

def checkDiagDesc(ligne,colonne):
	""" Checks wether the given square coordinate's diagonal (from top left to bottom right) contains a winning move
		returns the answer
 	"""
	adjacent = 0
	for x in range (3): 
		if(ligne + x + 1 < hauteur) and (colonne + x + 1 < largeur):
			if grille[ligne + x + 1][colonne + x + 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	for x in range (3):
		if(ligne - x - 1 >= 0) and (colonne - x - 1 >= 0):
			if grille[ligne - x - 1][colonne - x - 1] == symboles[currentplayer]:
				adjacent += 1
			else:
				break
	if adjacent == 3:
		return True
	else:
		return False															


def checkWinner(ligne,colonne):
	""" Checks wether the given square coordinate's is part of a winning move and updates currentplayer
		returns the answer
 	"""
 	global currentplayer
	if(checkColonne(ligne, colonne)):
		currentplayer = (currentplayer + 1) % 2 # change de joueur après verif de jouer pour que checkWinner soit fait avec le bon symbole
		return True
	elif(checkLigne(ligne,colonne)):
		currentplayer = (currentplayer + 1) % 2 # change de joueur avant de jouer pour que checkWinner soit fait avec le bon symbole
		return True
	elif (checkDiagAsc(ligne,colonne)):
		currentplayer = (currentplayer + 1) % 2 # change de joueur avant de jouer pour que checkWinner soit fait avec le bon symbole
		return True
	else:
		currentplayer = (currentplayer + 1) % 2 # change de joueur avant de jouer pour que checkWinner soit fait avec le bon symbole
		return checkDiagDesc(ligne,colonne)

def printgrille():
	""" Prints the game's grid and the current player in terminal
		NOTE: Used for debug
 	"""
	for x in range (hauteur):
		print ( str(x) + " " + str(grille[x]))
	
	print("    0    1    2    3    4    5    6 ")
	print ("c'est au joueur " + str(currentplayer+1) + " de jouer.")

















