class Controleur:
    def __init__(self, jeu):
        self.jeu = jeu
        self.tour_joueur_fini = False
        self.jeu_fini = False
        self.message_jeu_fini = " "

    def controle_bust_joueur(self):
        if self.jeu.compteur.valeur_joueur > 21:
            self.tour_joueur_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Vous avez dépasse 21 - VOUS AVEZ PERDU"
            print("Vous avez dépasse 21 - VOUS AVEZ PERDU")