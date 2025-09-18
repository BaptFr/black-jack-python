from PIL import Image
import os

# ---- paramètres
fichier_spritesheet = "1.2 Poker cards.png"
largeur_carte = 48
hauteur_carte = 64
nb_colonnes = 15
nb_lignes = 5   # 4 lignes de 13 + 1 ligne avec 6 cartes


os.makedirs("cartes_decoupees", exist_ok=True)

spritesheet = Image.open(fichier_spritesheet)


for ligne in range(nb_lignes):
    max_col = nb_colonnes if ligne < 4 else 6  # dernière ligne = 6 cartes seulement
    for col in range(max_col):
        x = col * largeur_carte
        y = ligne * hauteur_carte
        carte = spritesheet.crop((x, y, x + largeur_carte, y + hauteur_carte))
        carte.save(f"cartes_decoupees/carte_{ligne}_{col}.png")

print(" Découpage terminé, les cartes sont dans le dossier")
