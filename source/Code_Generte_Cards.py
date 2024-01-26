from PIL import Image, ImageDraw, ImageFont

def generer_cartes(cartes, dict_scores):
    for numero_carte, carte in enumerate(cartes, start=1):
        # Obtenir le score associé au numéro de carte depuis le dictionnaire
        score = dict_scores.get(numero_carte, 1)

        # Créer une image vide
        size = 4
        image = Image.new('RGB', (120*size, 200*size), color='lightgrey')

        # Charger une police différente (vous pouvez spécifier le chemin complet de votre police TrueType)
        font_size = 60*size
        font = ImageFont.truetype("arial.ttf", size=font_size)

        # Initialiser le dessinateur
        draw = ImageDraw.Draw(image)

        # Dessiner un rectangle pour la bordure
        draw.rectangle([10, 10, image.width-10, image.height-10], outline='black', width=2)

        # Coller l'image de la vachette
        vachette_size_color = (110 * size, 110 * size)
        vachette_size = (15*size, 15*size)
        vachette_y = 10*size

        image_vachette = Image.open("source/img/vachette.png").convert("RGBA")
        image_vachette_resized = image_vachette.resize(vachette_size)

        vachette_restant = score

        # Coller l'image de la vachette autant de fois que le score
        if numero_carte % 10 ==0:
            image_vachette_color = Image.open("source/img/vachette_pleine_rouge.png").convert('RGBA')
            image_vachette_resized_rouge = image_vachette_color.resize(vachette_size_color)
            image.paste(image_vachette_resized_rouge, (6 * size, 50 * size), image_vachette_resized_rouge)
            vachette_x = 37*size
            for i in range(score):
                image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                vachette_x += 16*size  # Ajuster la position pour les images suivantes

        elif numero_carte == 55:
            image_vachette_color = Image.open("source/img/vachette_shiny.png").convert('RGBA')
            image_vachette_resized_shiny = image_vachette_color.resize(vachette_size_color)
            image.paste(image_vachette_resized_shiny, (6 * size, 50 * size), image_vachette_resized_shiny)
            vachette_x = 30 * size
            for i in range(score):
                if i < 4:  # Les 4 premières vachettes centrées sur l'axe des x
                    image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                    vachette_x += 16*size  # Ajuster la position pour les images suivantes
                else:  # Les suivantes suivent en pyramide inversée en dessous des 4 premières
                    vachette_x -= 20*size
                    vachette_y = 26*size
                    image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                vachette_restant -= 1

        elif numero_carte % 5 == 0:
            vachette_x = 47 * size
            image_vachette_color = Image.open("source/img/vachette_pleine_verte.png").convert('RGBA')
            image_vachette_resized_verte = image_vachette_color.resize(vachette_size_color)
            image.paste(image_vachette_resized_verte, (6 * size, 50 * size), image_vachette_resized_verte)
            for i in range(score):
                image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                vachette_x += 16 * size  # Ajuster la position pour les images suivantes

        elif numero_carte % 11 == 0:
            image_vachette_color = Image.open("source/img/vachette_violette.png").convert('RGBA')
            image_vachette_resized_violette = image_vachette_color.resize(vachette_size_color)
            image.paste(image_vachette_resized_violette, (6 * size, 50 * size), image_vachette_resized_violette)
            vachette_x = 38 * size
            for i in range(score):
                if i < 3:  # Les 4 premières vachettes centrées sur l'axe des x
                    image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                    vachette_x += 16 * size  # Ajuster la position pour les images suivantes
                else:  # Les suivantes suivent en pyramide inversée en dessous des 4 premières
                    vachette_x -= 21* size
                    vachette_y = 26 * size
                    image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
                vachette_restant -= 1
        else:
            vachette_x = 53 * size
            image.paste(image_vachette_resized, (vachette_x, vachette_y), image_vachette_resized)
            image_vachette_color = Image.open("source/img/vachette_pleine_bleue.png").convert('RGBA')
            image_vachette_resized_blue = image_vachette_color.resize(vachette_size_color)
            image.paste(image_vachette_resized_blue, (6 * size, 50 * size), image_vachette_resized_blue)

        # Dessiner le numéro de carte au centre
        text = str(numero_carte)

        # Approximation de la largeur du texte
        if len(text) == 1:
            text_width = len(text) * (font_size // 2)
        elif len(text) == 2:
            text_width = len(text) * (font_size // 2) + 6
        else:
            text_width = len(text) * (font_size // 2) + 35
        x = (image.width - text_width) // 2
        y = (image.height - font_size) // 2

        # Dessiner le texte avec une bordure
        draw.text((x - 1, y - 1), text, font=font, fill='black')
        draw.text((x + 1, y - 1), text, font=font, fill='black')
        draw.text((x + 1, y + 1), text, font=font, fill='black')
        draw.text((x - 1, y + 1), text, font=font, fill='black')
        draw.text((x, y), text, font=font, fill='white')


        # Sauvegarder l'image dans le même répertoire que le script
        nom_fichier = f"source/cards/carte_{numero_carte}.jpg"
        image.save(nom_fichier)
        print(f"La carte {numero_carte} a été enregistrée sous {nom_fichier}")

def MakeDict():
    DictScore = {}
    for i in range(1, 105):
        if i % 10 == 0:
            DictScore[i] = 3
        elif i == 55:
            DictScore[i] = 7
        elif i % 5 == 0:
            DictScore[i] = 2
        elif i % 11 == 0:
            DictScore[i] = 5
        else:
            DictScore[i] = 1
    return DictScore

# Exemple d'utilisation
cartes = range(1, 105)  # Pour couvrir toutes les cartes de 1 à 105
dict_scores = MakeDict()
generer_cartes(cartes, dict_scores)
