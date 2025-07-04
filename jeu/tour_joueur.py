class TourJoueur:
    def __init__(self, partie, controleur):
        self.partie = partie
        self.controleur = controleur
        self.index_main_courante = 0

    def peut_doubler(self, index_main=0):
        if index_main >= len(self.partie.joueur):
            print(f"[DEBUG] Index {index_main} hors limite dans peut_doubler")
            return False

        main = self.partie.joueur[index_main]
        valeur = self.partie.compteur.calcul_valeur_main(main)
        return len(main) == 2 and valeur in [9, 10, 11]

    def peut_splitter(self, index_main=0):
        #Debug
        if index_main >= len(self.partie.joueur):
            print(f"[DEBUG] Index {index_main} hors limite dans peut_splitter")
            return False

        main = self.partie.joueur[index_main]
        if len(main) == 2 and main[0].valeur == main[1].valeur:
            return True
        return False

    def jouer(self, action, index_main=None):
        idx = index_main if index_main is not None else self.index_main_courante

        if action == "tirer":
            self.partie.tirer_carte_joueur(idx)
            valeur = self.partie.compteur.calcul_valeur_main(self.partie.joueur[idx])
            if valeur >= 21:
                self.passer_main_suivante()

        elif action == "doubler":
            if self.peut_doubler(idx):
                self.partie.action_doubler(idx)
                self.passer_main_suivante()

        elif action == "splitter":
            if self.peut_splitter(idx):
                self.partie.action_splitter(idx)
                self.index_main_courante = 0
                self.controleur.index_main_joueur = 0

        elif action == "stand":
            print("action stand")
            self.passer_main_suivante()

    def passer_main_suivante(self):
        self.index_main_courante += 1
        self.controleur.index_main_joueur = self.index_main_courante

        if self.index_main_courante >= len(self.partie.joueur):
            self.controleur.stand_joueur = True
            self.controleur.tour_croupier.demarrer()
