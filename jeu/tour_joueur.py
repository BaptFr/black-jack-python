
class TourJoueur:
    def __init__(self, partie, controleur):
        self.partie = partie
        self.controleur = controleur

    #Actiions spéciales
    def peut_doubler(self, index_main=0):
        main = self.partie.joueur[index_main]
        valeur = self.partie.compteur.calcul_valeur_main(main)
        if len(main) == 2 and valeur in [9, 10, 11]:
            return True

    def peut_splitter(self, index_main=0):
        main = self.partie.joueur[index_main]
        return len(main) == 2 and main[0].valeur == main[1].valeur


    def jouer(self, action, index_main=0):
        if action == "tirer":
            self.tirage.tirer_carte_joueur(index_main)
            print(f"Carte tirée : {self.tirage.joueur[index_main][-1]}")

        elif action == "doubler":
            if self.peut_doubler(index_main):
                self.tirage.action_doubler(index_main)
                print("Double effectué")
            else:
                print("Double impossible")

        elif action == "splitter":
            if self.peut_splitter(index_main):
                self.tirage.action_splitter(index_main)
                print("Split effectué")
            else:
                print("Split impossible")

        elif action == "stand":
            self.controleur.stand_joueur = True
            print("Le joueur reste (stand)")

        else:
            print("Erreur action Jouer")