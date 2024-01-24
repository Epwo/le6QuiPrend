104 cartes ( une chacune )


# classes POO

Classe Jeu
		attributs :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- isOver : check un joueur a il 66 pts ?<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- CartesTot : tt les 104 cartes.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- piles : liste de pile de cartes -> dict{"pile1":[1,55,103]} ..<br>
&nbsp;&nbsp;&nbsp;&nbsp;functions :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- __init__ : <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- create plateau -> choisis 4 cartes parmi la liste et les ajoutes dans piles.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- create DictScore<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - validCarte : pose la carte face caché<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - CleanPile : `(nomPile,player)` on désigne une pile : "pile1" et on la vide de ses cartes excepté la -1 dans player.score via<br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- CalculScore : `([int,int,...])` selon les regles de Round -> dictScore `= {10:3,20:3,...,55:7}` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Play : - (si tt les cartes sont validés)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- tri dans l'ordre croissant<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- compare a chaque pile de carte, on pose la carte la ou le $\delta$ est le + faible  et positif.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - une fois tt les cartes posées,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - on regarde la taille de chaque pile<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- IsReady : check pour chaque joueur l'attribut isReady, si 2/3 == 1 alors -> `DisplayClock`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- si 100% == 1 -> `play()`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - DisplayClock : affiche l'horloge de 30s  de timer. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- si a la fin du timer toujours pas choisi, prend une carte au hasard.<br>
<br>				  
Classe Joueur ( hérite ):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attributs :<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- cartes : 10 cartes aléatoires parmi la liste de 104 cartes <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- score : nb de vachettes<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nom : défaut = player<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-  isReady : le joueur a il validé sa carte?<br>

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
