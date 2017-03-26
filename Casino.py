# -*-coding:Latin1

import random
import os
import math

def roulette(caseChoisie):
	print("La roulette tourne...")
	caseGagnante =  random.randint(0, 49)
	print("Le numero gagnant est ", caseGagnante)
	if caseGagnante == caseChoisie :
		return 50
	elif (caseGagnante % 2) == (caseChoisie % 2):
		return 0.5
	else:
		return 0.0

argent = 50
continuerPartie = True

while continuerPartie :

	print("Vous commencez une nouvelle avec", argent, " argent")
	caseChoisie = -1
	while caseChoisie < 0 or caseChoisie > 49 :

		caseChoisie = input("Choisissez une case sur laquelle jouer : ")
		if(caseChoisie < 0) or caseChoisie > 49 :
			print("Veuilez entrer un numéro entre 0 et 49 !")

	mise = 0
	while mise <= 0 or mise > argent :

		mise = input("Veuillez entrer votre mise :")
		if mise < 0 :
			print("Veuillez entrer un chiffre positif !")
		elif mise > argent :
			print("Vous n'avez pas assez d'argent !")

	argent -= mise

	gain = roulette(caseChoisie)
	gain *= mise

	print("Bravo ! Vous avez gagné ", gain, " $$")
	argent += gain

	if argent == 0:
		continuerPartie = False



