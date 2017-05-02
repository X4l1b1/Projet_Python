# -*-coding:Latin-1 -*


largeur = 7
hauteur = 6
moves = 0
gagnant = -1
currentplayer = 0
symboles = ["X", "O"]



grille =[ ["-" for x in range (largeur)] for y in range (hauteur)]



def playMove(colonne):
	ligne = -1
	goodMove = False
#grille(2,1)= deuxième colone troisième ligne
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

def checkColone(ligne,colonne):
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
	if(checkColone(ligne, colonne)):
		return True
	elif(checkLigne(ligne,colonne)):
		return True
	elif (checkDiagAsc(ligne,colonne)):
		return True
	else:
		return checkDiagDesc(ligne,colonne)

def printgrille():
	#grille(2,1)= deuxième colone troisième ligne
	for x in range (hauteur):
		print ( str(x) + " " + str(grille[x]))
	
	print("    0    1    2    3    4    5    6 ")
	print ("c'est au joueur " + str(currentplayer+1) + " de jouer.")

















