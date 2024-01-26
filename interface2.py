import pygame
from PIL import Image


class GameBoard:
    def __init__(self, nbPlayer=2, size=3):
        self.nbPlayer = nbPlayer
        self.size = size

    # Afficher le plateau de jeu pour un joueur
    def DisplayBoard(self, size):
        # Initialiser pygame
        pygame.init()

        # Paramètrer l'affichage
        width, height = 400 * size, 250 * size
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Le 6 qui prend")

        # Remplir le fond d'une couleur bleu clair
        screen.fill((173, 216, 230))

        # Ajout du logo en fond à la taille voulue
        original_image = Image.open("source/img/LOGO.png")
        resized_image = original_image.resize((150 * size, 150 * size))

        resized_image = resized_image.convert("RGBA")
        image_surface = pygame.image.fromstring(resized_image.tobytes(), resized_image.size,
                                                resized_image.mode).convert_alpha()
        image_rect = image_surface.get_rect()
        player_pos = (width // 2, height // 2)
        screen.blit(image_surface, (player_pos[0] - image_rect.width // 2, player_pos[1] - image_rect.height // 2))

        ### Ajout des paramètres joueurs
        # Affichage du tableau des scores en haut à gauche
        # [element_player, ..  ]
        font = pygame.font.Font(None, 36)
        score_text = font.render("Scores: 1000", True, (255, 255, 255))  # Modifier le score en conséquence
        score_rect = score_text.get_rect()
        score_rect.topleft = (20, 20)  # Modifier la position ici
        screen.blit(score_text, score_rect)

        # Mise à jour de l'affichage
        pygame.display.flip()

        # Boucle
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Exit
        pygame.quit()

# Exemple d'utilisation
instance = GameBoard()
instance.DisplayBoard(3)  # Utilisez la taille souhaitée
