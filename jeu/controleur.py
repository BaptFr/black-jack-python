from .compteur import Compteur

class Controleur:
    def __init__(self, partie):
        self.partie = partie
        self.tour_joueur_fini = False
        self.stand_joueur = False
        self.tour_croupier_fini = False
        self.stand_croupier = False
        self.jeu_fini = False
        self.message_jeu_fini = " "
        #Main en cours pour gérer split:
        self.index_main_joueur = 0


    def controle_blackJack(self):
         #main en cours
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]
        valeur_croupier = self.partie.compteur.valeur_croupier
        if valeur_main == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " BLACKJACK - VOUS AVEZ GAGNÉ"
        elif valeur_croupier == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a un BLACKJACK - VOUS AVEZ PERDU"

    #Contrôle fin de jeu
    def controle_fin_jeu(self):
        #main en cours
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]
        valeur_croupier = self.partie.compteur.valeur_croupier
        if valeur_main > 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " Au dessus de 21 - VOUS AVEZ PERDU"
        elif valeur_main == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " VOUS AVEZ GAGNÉ"
        elif valeur_croupier > 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a dépassé 21 - VOUS AVEZ GAGNÉ"
        elif valeur_croupier == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " VOUS AVEZ PERDU"

        # Comparaison des scores (après stands)
        elif self.stand_croupier and self.stand_joueur:
            self.jeu_fini = True
            if valeur_main > valeur_croupier:
                self.message_jeu_fini = f"Vous avez une meilleur main - VOUS AVEZ GAGNÉ"
            elif valeur_main < valeur_croupier:
                self.message_jeu_fini = f"Le croupier a une meilleur main -VOUS AVEZ PERDU"
            else:
                self.message_jeu_fini = f"ÉGALITÉ"

        if self.jeu_fini:
            print(self.message_jeu_fini)
