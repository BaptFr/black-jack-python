class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
        self.face_visible = True

    def image_path(self):
        valeur = self.valeur.lower()
        couleur = self.couleur.lower()
        nom_fichier = f"{valeur}_{couleur}.png"
        return f"assets/images/cartes/{nom_fichier}"