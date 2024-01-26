import pygame, os, time
from PIL import Image


class GameInterface:
    def __init__(self, size):
        # Paramètrer l'affichage
        self.size = size
        self.width, self.height = 400 * size, 250 * size
        self.player_pos = (self.width // 2, self.height // 2)

        # Initialiser pygame
        pygame.init()

        # Créer la fenêtre
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Le 6 qui prend")

        # Ajouter les paramètres joueurs
        self.font = pygame.font.Font(None, 36)
        # !SET SCORE!
        self.score_text = self.font.render("Votre score: 1000", True, (255, 255, 255))
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (20, 20)  # Modifier la position ici

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

    def SetScore(self, score):
        self.score_text = self.font.render("Votre score: " + str(score), True, (255, 255, 255))

    def displayPlayers(self, players):
        # Font for displaying player names and scores
        playerFont = pygame.font.Font(None, 36)
        scoreFont = pygame.font.Font(None, 20)

        # Vertical spacing between player names and scores
        spacing = 40

        for i, player in enumerate(players):
            size = self.size
            # Display player name
            player_name_text = playerFont.render(player["name"], True, (255, 255, 255))
            player_name_rect = player_name_text.get_rect()
            player_name_x = 350*size  # Adjust the starting position of player names
            player_name_y = i * (player_name_rect.height + spacing) + 40  # Adjust vertical position
            self.screen.blit(player_name_text, (player_name_x, player_name_y))
            if player["isReady"]:
                TickText = playerFont.render("√", True, (255, 255, 255))
                self.screen.blit(TickText, (player_name_x-10*size, player_name_y))

            # Display player score underneath the name
            player_score_text = scoreFont.render(f"{player['score']} vachettes ", True, (255, 255, 255))
            player_score_rect = player_score_text.get_rect()
            player_score_x = 350*size  # Adjust the starting position of player scores
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

        # Afficher le score
        self.screen.blit(self.score_text, self.score_rect)

        # Mise à jour de l'affichage
        pygame.display.flip()

    def displayCards(self, cards, mouse_pos):
        # Afficher les cartes
        for i, card in enumerate(cards):
            # Get the original and hovered images corresponding to the card number
            original_image = self.card_images.get(card)
            hovered_image = self.hovered_images.get(card)

            if original_image and hovered_image:
                # Calculer la position horizontale de la carte en fonction de l'index
                card_x = i * (hovered_image.get_width()) + 20  # Modifier la position de départ ici

                # Calculer la position verticale de la carte pour la centrer
                card_y = (self.size * 230) - (
                            hovered_image.get_height() / 2)  # Modifier la position verticale ici si nécessaire

                # Check if the mouse is over the image
                image_rect = pygame.Rect(card_x, card_y, hovered_image.get_width(), hovered_image.get_height())
                is_hovered = image_rect.collidepoint(mouse_pos)

                # Display the hovered image if the mouse is over, otherwise display the original image
                display_image = hovered_image if is_hovered else original_image

                # Afficher l'image à la position calculée
                self.screen.blit(display_image, (card_x, card_y))

        # Mise à jour de l'affichage
        pygame.display.flip()

    def checkCardClick(self, cards, mouse_pos):
        card_spacing = 40

        for i, card in enumerate(cards):
            card_image = self.card_images.get(card)

            if card_image:
                card_x = i * (card_image.get_width() + card_spacing) + 20
                card_y = (self.size * 230) - (card_image.get_height() / 2)

                # Check if the mouse is over the card
                card_rect = pygame.Rect(card_x, card_y, card_image.get_width(), card_image.get_height())
                if card_rect.collidepoint(mouse_pos):
                    return card

        return None

    def displayPiles(self, piles):
        # Afficher les cartes
        for pile_index, pile in enumerate(piles):
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

    def runGameLoop(self):
        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the mouse position
                    mouse_pos = pygame.mouse.get_pos()

                    # Check if a card was clicked
                    clicked_card = self.checkCardClick([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], mouse_pos)
                    # If a card was clicked, print a message
                    if clicked_card is not None:
                        print(f"Card {clicked_card} clicked!")

            # Appeler la méthode pour afficher le tableau
            self.displayBoard(self.size)
            mouse_pos = pygame.mouse.get_pos()
            # !GET CARDS!
            # !GET PILES!
            self.displayCards([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], mouse_pos=mouse_pos)
            self.displayPiles([[70,71,75], [80,104], [55,58,61,74,79], [68]])
            self.displayPlayers([{"name": "Joueur 1", "score": 152,"isReady":False}, {"name": "Joueur 2", "score": 666,"isReady":True}])
            pygame.display.flip()
            time.sleep(0.05)
        # Quitter pygame une fois la boucle terminée
        pygame.quit()


# Exemple d'utilisation
if __name__ == "__main__":
    interface = GameInterface(size=3)
    interface.runGameLoop()
