
class TourJoueur:
    def __init__(self, partie, controleur):
        self.partie = partie
        self.controleur = controleur
        self.index_main_courante = 0

    #Actions spéciales
    def peut_doubler(self, index_main=0):
        main = self.partie.joueur[index_main] ####Nombre de mains du joueur###
        valeur = self.partie.compteur.calcul_valeur_main(main)
        if len(main) == 2 and valeur in [9, 10, 11]:
            return True

#DEBUG ***************************
    def peut_splitter(self, index_main=0):
        main = self.partie.joueur[index_main]
        print(f"[DEBUG] Test split : {main}")
        if len(main) == 2 and main[0].valeur == main[1].valeur:
            print("DEBUG: peut_splitter = True")
            return True
        print("DEBUG: peut_splitter = False")
        return False

    def jouer(self, action, index_main=None):
        idx = index_main if index_main is not None else self.index_main_courante
        if action == "tirer":
            self.partie.tirer_carte_joueur(idx)
            print(f"Carte tirée : {self.partie.joueur[idx][-1]}")
            #Vérif. Bust
            valeur = self.partie.compteur.calcul_valeur_main(self.partie.joueur[idx])
            if valeur > 21:
                print(f"main {idx} bustée")
                self.passer_main_suivante()
                return
            elif valeur ==  21:
                print(f"main {idx}: 21 atteeint")
                self.passer_main_suivante()
                return

        elif action == "doubler":
            if self.peut_doubler(idx):
                self.partie.action_doubler(idx)
                print("Double effectué")
                self.passer_main_suivante()
            else:
                print("Double impossible")

        elif action == "splitter":
            if self.peut_splitter(idx):
                self.partie.action_splitter(idx)
                print("Split effectué")
                self.index_main_courante = 0
                self.controleur.index_main_joueur = 0
            else:
                print("Split impossible")

        elif action == "stand":
            print(f"Main {idx} reste (stand)")
            self.passer_main_suivante()

        else:
            print("Erreur action Jouer")

    def passer_main_suivante(self):
        #Pour que l'index sot égale au n° de la main:
        self.controleur.index_main_joueur = self.index_main_courante
        self.index_main_courante += 1
        print(f"[DEBUG] index_main_courante={self.index_main_courante}, nb mains={len(self.partie.joueur)}")

        #Si toutes les main jouées => stand
        if self.index_main_courante == len(self.partie.joueur):
            self.controleur.stand_joueur = True
            self.controleur.tour_croupier.demarrer()
            print("Fin du tour joueur, passage au tour croupier")
        else:
            print("Passage main suivante du joueur")