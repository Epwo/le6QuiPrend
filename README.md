104 cartes ( une chacune )


# classes POO

Classe Jeu
		attributs :
  			- isOver : check un joueur a il 66 pts ?
			- CartesTot : tt les 104 cartes.
			- piles : liste de pile de cartes -> dict{"pile1":[1,55,103]} ..
		functions :
			- __init__ : 
				- create plateau -> choisis 4 cartes parmi la liste et les ajoutes dans piles.
				- create DictScore
			- validCarte : pose la carte face caché
			- CleanPile : `(nomPile,player)` on désigne une pile : "pile1" et on la vide de ses cartes excepté la -1 dans player.score via 
			- CalculScore : `([int,int,...])` selon les regles de Round -> dictScore `= {10:3,20:3,...,55:7}` 
			- Play : - (si tt les cartes sont validés)
				  - tri dans l'ordre croissant
				  - compare a chaque pile de carte, on pose la carte la ou le $\delta$ est le + faible  et positif.
				  - une fois tt les cartes posées,
				  - on regarde la taille de chaque pile
			  - IsReady : check pour chaque joueur l'attribut isReady, si 2/3 == 1 alors -> `DisplayClock`
				  - si 100% == 1 -> `play()`
			  - DisplayClock : affiche l'horloge de 30s  de timer. 
				  - si a la fin du timer toujours pas choisi, prend une carte au hasard.
				  
Classe Joueur ( hérite ):
	attributs :
		- cartes : 10 cartes aléatoires parmi la liste de 104 cartes
		- score : nb de vachettes
		- nom : défaut = player
		-  isReady : le joueur a il validé sa carte?

# Image du fonctionnement Interface

![[6quiprend schema.jpg|]]

# Pré round
 10 cartes chacun -> a moduler si on veut pour la longueur du jeu
# round
## cartes multiples de 10
- 3 vachettes
## cartes mutiples de 5
- 2 vachettes
(qui finissent par 5)
## cartes mutiples de 11
( SAUF LE 55 )
- 5 vachettes
## le 55
- 7 vachettes
# Post round
-> ask ready for the next round ? -> dialog box 
garder les pts entre chaque tour
!! Si joueur.pts() >= 66 -> fin du jeu il a perdu.
