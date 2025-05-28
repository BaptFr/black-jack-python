

class Compteur:
    def __init__(self):
        self.valeur_joueur= 0
        self.valeur_croupier = 0
        self.valeurs_cartes = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "V": 10, "D": 10, "R": 10, "As": 11
        }

    def calcul_valeur_main(self, main):
        total_main = 0
        for carte in main:
            #d'abord reprendre valeur (string)
            valeur = carte.valeur
            #utiliser la conversion en int
            total_main = total_main + self.valeurs_cartes[valeur]
        return total_main

    def mise_a_j_valeur_main(self, jeu):
        self.valeur_joueur = self.calcul_valeur_main(jeu.joueur)
        self.valeur_croupier = self.calcul_valeur_main(jeu.croupier)

    def verification_black_jack(self, jeu):
        self.mise_a_j_valeur_main(jeu)
        main_joueur = self.valeur_joueur
        main_croupier = self.valeur_croupier

        if main_joueur == 21 and main_croupier ==21:
            return "blackjack_egalité"
        if main_joueur == 21:
            return"blackjack_joueur"
        if main_croupier == 21:
            return "blackjack_croupier"
        else:
            return "continuer"
