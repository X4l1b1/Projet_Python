# -*-coding:Latin1
largeur = 3
hauteur = 3
moves = 0
gagnant = -1
currentP = 0
symbols = ['X', 'O']

grille = [ ['-' for x in range(largeur)] for y in range(hauteur)]

def printGrille():
	#grille[2][1] = 2e colonne 3e ligne
	for x in range(hauteur):
		print(grille[x])

def askMove():
	(ligne, colonne) = (-1, -1)
	goodMove = False


	while not goodMove:

		(ligne, colonne) = (input("indiquez la ligne"), input("indiquez la colonne"))
		if(ligne >= 0 and ligne < hauteur and colonne >= 0 and colonne < largeur):
			if(grille[colonne][ligne] == '-'):
				goodMove = True

	return (ligne, colonne)

def playAndCheckEnd(symbol, ligne, colonne):

	grille[ligne][colonne] = symbol
	#isDiag = False

	# Verifie si la ligne est gagnante
	if(grille[ligne][(colonne + 1) % largeur]== symbol) and (grille[ligne][(colonne + 2) % largeur] == symbol):
		return True;

	#Verifie si la colonne est gagnante
	if(grille[(ligne + 1) % hauteur] == symbol) and (grille[(ligne + 2) % hauteur] == symbol):
		return True

#	for x in range(hauteur):
#		for y in range(largeur):
#			if(ligne, colonne) == (x, largeur - y) or (hauteur -x, y):
#				isDiag = True

	#Si l'élément est sur une diagonale MARCHE UNIQUEMENT POUR 3X3
	if(colonne == ligne):
		#On vérifie celle de droite à gauche
		return (grille[(ligne+1)% hauteur][(colonne+1)%largeur] == symbol) and (grille[(ligne+2)%hauteur][(colonne + 2)%largeur] == symbol)

	#Puis on vérifie la deuxieme
	elif (ligne, colonne) == (0, largeur - 1) or (ligne, colonne) == (hauteur -1, 0):
		return (grille[1][1] == symbol) and (grille[colonne][ligne] == symbol)
	#Sinon personne n'a gagné et la partie continue
	else:
		return False


#Boucle du jeu
while(moves < largeur*hauteur) and gagnant < 0:

	printGrille()

	(ligne, colonne) = askMove()

	gagne = playAndCheckEnd(symbols[currentP], ligne, colonne)

	if gagne :
		gagnant = currentP;
	else:
		currentP = (currentP + 1) % 2


printGrille()
#Fin du Jeu
if(gagnant == -1):
	print("It's a tie!")
elif(gagnant == 0):
	print("Player 1 wins !")
else:
	print("Player 2 wins !")

