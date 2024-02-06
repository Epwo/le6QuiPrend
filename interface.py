import pygame, os, time
from PIL import Image
import tkinter as tk
from tkinter import messagebox

class GameInterface:
    def __init__(self, size):
        # Paramètrer l'affichage
        self.NbPlayerMe = None
        self.clicked_card = None
        self.piles = [[], [], [], []]
        self.mouse_pos = None
        self.cards = []
        self.players = []
        self.size = size
        self.width, self.height = 430 * size, 250 * size
        self.player_pos = (self.width // 2, self.height // 2)

        # Initialiser pygame
        pygame.init()
        self.font = pygame.font.Font(None, 36)

        # Créer la fenêtre
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Le 6 qui prend")

        self.card_images = {}
        self.hovered_images = {}
        for i in range(1, 105):  # Assuming card numbers range from 1 to 10
            image_path = f"source/cards/carte_{i}.jpg"  # Adjust the path based on your directory structure
            if os.path.exists(image_path):
                original_image = pygame.image.load(image_path)
                scaled_image = pygame.transform.scale(original_image, (30 * size, 50 * size))
                self.card_images[i] = scaled_image
                self.hovered_images[i] = pygame.transform.scale(original_image,
                                                                (40 * size, 60 * size))  # Adjust the hover size

            else:
                print(f"Image not found: {image_path}")

    def GetPileChoice(self):
        return self.PileChoice

    def SetScore(self, score):
        self.score_text = self.font.render("Votre score: " + str(score), True, (255, 255, 255))

    def SetPlayers(self, players):
        self.players = players

    def SetCards(self, cards):
        self.cards = cards

    def SetWhoIAm(self, nb):
        self.NbPlayerMe = nb

    def SetPiles(self, piles):
        self.piles = piles

    def Winner(self, text):
        fenetre_principale = tk.Tk()
        fenetre_principale.title("Félicitations !")

        # Définir la taille et la position de la fenêtre pop-up
        fenetre_principale.geometry("400x200+400+200")

        # Ajouter une couleur de fond et une bordure
        fenetre_principale.configure(bg="#FFFFCC", bd=10)

        # Créer un cadre pour organiser les éléments
        frame = tk.Frame(fenetre_principale, bg="#FFFFCC")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Ajouter un label avec le message de victoire
        label_texte = tk.Label(frame, text=text, font=("Helvetica", 16), bg="#FFFFCC")
        label_texte.pack(pady=10)

        # Ajouter un bouton pour fermer la fenêtre pop-up
        bouton_fermer = tk.Button(frame, text="Fermer", command=fenetre_principale.destroy)
        bouton_fermer.pack(pady=10)

        # Lancer la boucle principale de la fenêtre pop-up
        fenetre_principale.mainloop()

    def PopUp(self, nbPoint):
        def on_bouton_click(PileChoice):
            print(f"----------\n"
                  f"Choix du bouton : Pile {PileChoice} qui vaut {nbPoint[PileChoice]} vachettes")
            fenetre_principale.destroy()  # Fermer la fenêtre après avoir affiché le choix
            self.PileChoice = PileChoice

        fenetre_principale = tk.Tk()
        label_texte = tk.Label(fenetre_principale, text="Veuillez choisir une des piles que vous allez remplacer. Vous récupérerez les vachettes de la pile choisie.")
        label_texte.pack(pady=10)

        # Création d'un bouton pour afficher la fenêtre pop-up
        for i in range(0, 4):
            bouton_pile = tk.Button(fenetre_principale, text=f"Pile {i} qui vaut {nbPoint[i]} vachettes")
            bouton_pile.pack(pady=10)
        # Boucle principale
        fenetre_principale.mainloop()

    def displayPlayers(self):
        # Font for displaying player names and scores
        playerFont = pygame.font.Font(None, 36)
        scoreFont = pygame.font.Font(None, 20)

        # Vertical spacing between player names and scores
        spacing = 40

        for i, player in enumerate(self.players):
            size = self.size
            # Display player name
            if player["name"][-1] == str(self.NbPlayerMe):
                couleur = (255, 0, 0)
            else:
                couleur = (255, 255, 255)
            player_name_text = playerFont.render(player["name"], True, couleur)
            player_name_rect = player_name_text.get_rect()
            player_name_x = 350 * size  # Adjust the starting position of player names
            player_name_y = i * (player_name_rect.height + spacing) + 40  # Adjust vertical position
            self.screen.blit(player_name_text, (player_name_x, player_name_y))
            if player["isReady"]:
                TickText = playerFont.render("√", True, (255, 255, 255))
                self.screen.blit(TickText, (player_name_x - 10 * size, player_name_y))

            # Display player score underneath the name
            player_score_text = scoreFont.render(f"{player['score']} vachettes ", True, (255, 255, 255))
            player_score_rect = player_score_text.get_rect()
            player_score_x = 350 * size  # Adjust the starting position of player scores
            player_score_y = player_name_y + player_name_rect.height  # Place score underneath the name
            self.screen.blit(player_score_text, (player_score_x, player_score_y))

        # Mise à jour de l'affichage
        pygame.display.flip()

    def displayBoard(self, size):
        # Remplir le fond d'une couleur bleu clair
        self.screen.fill((173, 216, 230))

        # Charger et redimensionner le logo
        original_image = Image.open("source/img/LOGO.png")
        resized_image = original_image.resize((150 * size, 150 * size))
        resized_image = resized_image.convert("RGBA")
        image_surface = pygame.image.fromstring(resized_image.tobytes(), resized_image.size,
                                                resized_image.mode).convert_alpha()
        image_rect = image_surface.get_rect()
        # Afficher le logo

        self.screen.blit(image_surface,
                         (self.player_pos[0] - image_rect.width // 2, self.player_pos[1] - image_rect.height // 2))

        # Mise à jour de l'affichage
        pygame.display.flip()

    def displayCards(self):
        # Afficher les cartes
        for i, card in enumerate(self.cards):
            # Get the original and hovered images corresponding to the card number
            original_image = self.card_images.get(card)
            hovered_image = self.hovered_images.get(card)

            if original_image and hovered_image:
                # Calculer la position horizontale de la carte en fonction de l'index
                card_x = i * (hovered_image.get_width()) + 60  # Modifier la position de départ ici

                # Calculer la position verticale de la carte pour la centrer
                card_y = (self.size * 230) - (
                        hovered_image.get_height() / 2)  # Modifier la position verticale ici si nécessaire

                # Check if the mouse is over the image
                image_rect = pygame.Rect(card_x, card_y, hovered_image.get_width(), hovered_image.get_height())
                is_hovered = image_rect.collidepoint(self.mouse_pos)

                # Display the hovered image if the mouse is over, otherwise display the original image
                display_image = hovered_image if is_hovered else original_image

                # Afficher l'image à la position calculée
                self.screen.blit(display_image, (card_x, card_y))

        # Mise à jour de l'affichage
        pygame.display.flip()

    def checkCardClick(self):
        card_spacing = 40

        for i, card in enumerate(self.cards):
            card_image = self.card_images.get(card)

            if card_image:
                card_x = i * (card_image.get_width() + card_spacing) + 20
                card_y = (self.size * 230) - (card_image.get_height() / 2)

                # Check if the mouse is over the card
                card_rect = pygame.Rect(card_x, card_y, card_image.get_width(), card_image.get_height())
                if card_rect.collidepoint(self.mouse_pos):
                    return card

        return None

    def displayPiles(self):
        # Afficher les cartes
        for pile_index, pile in enumerate(self.piles):
            for card_index, card in enumerate(pile):
                card_image = self.card_images.get(card)
                if card_image:
                    # position x en fonction de l'index de la carte dans la pile
                    card_x = card_index * (card_image.get_width() + 10) + 50
                    # position y en fonction de l'index de la pile
                    card_y = (self.size * 40) * pile_index - (card_image.get_height() / 2) + 125
                    # Afficher l'image à la position calculée
                    self.screen.blit(card_image, (card_x, card_y))

        # Mise à jour de l'affichage
        pygame.display.flip()

    def GetClickedCards(self):
        return self.clicked_card

    def runGameLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_pos = pygame.mouse.get_pos()
                # Check if a card was clicked
                self.clicked_card = self.checkCardClick()
                # If a card was clicked, print a message
                if self.clicked_card is not None:
                    print(f"Card {self.clicked_card} clicked!")

        # Appeler la méthode pour afficher le tableau
        self.displayBoard(self.size)
        self.mouse_pos = pygame.mouse.get_pos()
        self.displayCards()
        self.displayPiles()
        self.displayPlayers()

        # Afficher la fenêtre pop-up si elle existe
        pygame.display.flip()
        time.sleep(0.05)

    # Quitter pygame une fois la boucle terminée
    pygame.quit()


if __name__ == "__main__":
    interface = GameInterface(size=3)
    interface.SetCards([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    interface.SetPiles([[1, 2, 3, 4], [55, 23, 64], [1], [5]])
    interface.SetPlayers([{"name": "Joueur 1", "score": 0, "isReady": True},
                          {"name": "Joueur 2", "score": 0, "isReady": False},
                          {"name": "Joueur 3", "score": 0, "isReady": False}])
    #interface.PopUp([20, 10, 41, 41])
    interface.Winner()
    while 1:
        interface.runGameLoop()
        #interface.PopUp([20, 10, 41, 41])
