from .compteur import Compteur

class Controleur:
    def __init__(self, jeu):
        self.jeu = jeu
        self.tour_joueur_fini = False
        self.stand_joueur = False
        self.tour_croupier_fini = False
        self.stand_croupier = False
        self.jeu_fini = False
        self.message_jeu_fini = " "

    def controle_fin_jeu(self):
        #BLACKJACKs
        if self.jeu.compteur.valeur_joueur > 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Vous avez dépasse 21 - VOUS AVEZ PERDU"
            print("Vous avez dépasse 21 - VOUS AVEZ PERDU")
        elif self.jeu.compteur.valeur_croupier > 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a dépassé 21 - VOUS AVEZ GAGNÉ"
            print("Le croupier a dépassé 21 - VOUS AVEZ GAGNÉ")

        #Comparaison des scores
        elif self.stand_croupier and self.stand_joueur:
            self.jeu_fini = True
            if self.jeu.compteur.valeur_joueur > self.jeu.compteur.valeur_croupier:
                self.message_jeu_fini = "VOUS AVEZ GAGNÉ"
                print("VOUS AVEZ GAGNÉ")
            elif self.jeu.compteur.valeur_joueur < self.jeu.compteur.valeur_croupier:
                self.message_jeu_fini = "VOUS AVEZ PERDU"
                print("VOUS AVEZ PERDU")
            elif self.jeu.compteur.valeur_joueur == self.jeu.compteur.valeur_croupier:
                self.message_jeu_fini = "ÉGALITÉ"
                print("ÉGALITÉ")
            print(self.message_jeu_fini)
