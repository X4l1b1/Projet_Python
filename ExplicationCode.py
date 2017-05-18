
def playMove(colonne):
	""" Method which, given a column index, checks wether :
				- the index is not out of bounds
				- the column isn't full
		if so, it fills the first valid element of the board with the current player's symbol
		updates current player's value
		returns anyway the move's row and validity
 	"""
	global currentplayer # global --> indiquer qu'on veut accéder a la variable globale et pas en créer une locale
	ligne = -1			 #valeur impossible pour ^etre sur de pas satisfaire les conditions par defaut
	goodMove = False	 # pareil
	for y in range (hauteur): # on boucle sur chaque ligne de la colonne
		if (grille[hauteur -1 - y][colonne] == "-"): # Si la case contient le symbole de départ, alors la case est libre (on part hauteur - 1 - y parce que on part du bas)
			goodMove = True		#coup valide
			ligne = hauteur -1 -y	# index case courant
			break		# on sort de la boucle
		if not goodMove:		
					continue	# On continue 
	if goodMove: 
		grille [ligne][colonne] = symboles[currentplayer] # On remplit la grille
	
	return ligne, goodMove # retourne le numero (pour pouvoir colorier le rond) et goodmove (pour le dire a l'interface)


	def event_player(event):
	""" Method called uppon a player's click on a game column
		if game is finished, does nothing
		else checks validity of the move using motor's method
		if the move is valid, colors the corresponding circle and update current_player
 	"""
	global current_player # global pour présciser qu'on veut pas redéfinir la variable en local
	global done			  # PAREIL
	if not done :		 # Si le jeu est terminé, on ne fait rien en cas de click
		column = event.widget.winfo_x()/WDTH_COL 	#winfo_x nous donne la coordonée x (horizontale) du clic dans LA FENETRE (PAS LA COLONNE)
		ligne, goodMove = motor.playMove(column)   # On appelle playMove pour valider le coup
	
		if goodMove:								#si il est valide, on fait quelque chose, sinon rien n'est fait
			changecolor(event.widget, current_player, ligne) # changer la couleur des rond (colonne, index pour la couleur, ligne pour la case) aussi le petit en bas
			if motor.checkWinner(ligne, column):		# on verifie si le coup est gagnat
				done = 1								# si oui partie terminée
				winner = "Le joueur " + str(current_player) +" a gagne !" 
				text.set(winner) # On affiche le gagnant en changeant sa variable de texte
			current_player = (current_player + 1) % 2  # Dans tous les cas, on met a jour le joueur courant