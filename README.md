# Le principe de jeu
Chaque joueur se voit attribuer 10 cartes de 1 à 104 telle que celle-ci :


![carte_66.jpg](https://raw.githubusercontent.com/Epwo/le6QuiPrend/main/source/img/carte_66.jpg)

Chaque tour les joueurs choisissent une carte. Une fois chaque joueur ayant choisi une carte, la plus petite commence, et les cartes se placent au plus proche positif des cartes de la pile.

Une fois qu'un joueur pose la 6e carte de la pile, il se voit contraint de récupérer toutes les cartes de la pile (excepté la sienne qu'il laisse en tant que nouvelle pile)
Il compte ensuite le nombre de vachettes en haut de chaque carte, cela fait son score qu'on comparera a celui des autres joueurs en fin de partie.

Le joueur avec le score le plus faible sera le vainqueur.
# L'installation
Il faut qu'un joueur lance le serveur, (en parallèle du coté client )
Si un serveur est lancé, il faut modifier l'IP dans le fichier `Mutliplayer/master_ip.txt` selon l'ip du pc source, avec la commande `ipconfig` .

De même manière les 'clients' devront changer la valeur de Master_ip.txt par l'ip du pc cible.

# Release - current working version 
[cliquez ici](https://github.com/Epwo/le6QuiPrend/tree/0356746fa830b79f6250e3349ddfd1269af57a14)
Suite a un merge problème, le reste n'est plus opérationnel 🫣🫣

# Exemple Jeu

![[Pasted image 20240207165316.png]]
# Architecture 

 
# Présentation
[Lien de la présentation Gslides](https://docs.google.com/presentation/d/1HV2KnmRzA54FXpBaO3FKxhuZdyvwR8Y3CSQ147IN05Q/edit#slide=id.g2b7613a9a0b_0_26)
