class TourJoueur:
    def __init__(self, partie, controleur):
        self.partie = partie
        self.controleur = controleur
        self.index_main_courante = 0


    def peut_splitter(self, index_main=0):
        #Debug
        if index_main >= len(self.partie.joueur):
            print(f"[DEBUG] Index {index_main} hors limite dans peut_splitter")
            return False

        main = self.partie.joueur[index_main]
        # Deux cartes seulement
        if len(main) != 2:
            return False

        #Correction: Règles Françaises. Comparaison des valeurs numériques des cartes
        valeur1 = self.partie.compteur.valeurs_cartes [main[0].valeur]
        valeur2 = self.partie.compteur.valeurs_cartes [main[1].valeur]
        if valeur1 != valeur2:
            return False

        #Max 4 split -> 4 mains
        if len(self.partie.joueur) >= 4:
            print("[SPLIT INTERDIT] Nombre maximum de mains atteint")
            return False
        #2x split As interdit
        if main[0].valeur == "As":
            if hasattr(self.partie, "as_deja_split") and self.partie.as_deja_split:
                print("[SPLIT INTERDIT] Re-split des As interdit")
                return False
        return True


    def peut_doubler(self, index_main=0):
        if index_main >= len(self.partie.joueur):
            print(f"[DEBUG] Index {index_main} hors limite dans peut_doubler")
            return False

        main = self.partie.joueur[index_main]
        valeur = self.partie.compteur.calcul_valeur_main(main)
        return len(main) == 2 and valeur in [9, 10, 11]


    def jouer(self, action, index_main=None):
        idx = index_main if index_main is not None else self.index_main_courante

        if action == "tirer":
            self.partie.tirer_carte_joueur(idx)
            valeur = self.partie.compteur.calcul_valeur_main(self.partie.joueur[idx])
            if valeur >= 21:
                self.passer_main_suivante()

        elif action == "doubler":
            if self.peut_doubler(idx):
                mise_actuelle = self.partie.mises[idx]
                if self.partie.solde >= mise_actuelle:
                    self.partie.solde -= mise_actuelle
                    self.partie.mises[idx] = mise_actuelle * 2
                    self.partie.action_doubler(idx)
                    print("action doubler")
                    self.passer_main_suivante()
                else:
                    print("Solde insuffisant pour doubler")

        elif action == "splitter":
            if self.peut_splitter(idx):
                mise_actuelle = self.partie.mises[idx]
                if self.partie.solde >= mise_actuelle:
                    self.partie.solde -= mise_actuelle
                    self.partie.action_splitter(idx)
                    self.index_main_courante = 0
                    self.controleur.index_main_joueur = 0
                    print("action splitter")
                else:
                    print("Solde insuffisant pour splitter")

        elif action == "stand":
            print("action stand")
            self.passer_main_suivante()

    def passer_main_suivante(self):
        self.index_main_courante += 1
        self.controleur.index_main_joueur = self.index_main_courante

        if self.index_main_courante >= len(self.partie.joueur):
            print('stand jouer ...')
            self.controleur.stand_joueur = True
            self.controleur.tour_joueur_fini = True
            self.controleur.tour_croupier.demarrer()
