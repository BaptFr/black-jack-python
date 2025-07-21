from .compteur import Compteur
from .tour_croupier import TourCroupier

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
        self.tour_croupier = TourCroupier(partie, self)


    def controle_blackJack(self):
         #main en cours
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]
        valeur_croupier = self.partie.compteur.valeur_croupier
        if valeur_main == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " BLACKJACK - VOUS AVEZ GAGNÉ"
        elif  valeur_main > 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = " Vous avez dépassé 21 - VOUS AVEZ PERDU"
        elif valeur_croupier == 21:
            self.tour_joueur_fini = True
            self.tour_croupier_fini = True
            self.jeu_fini = True
            self.message_jeu_fini = "Le croupier a un BLACKJACK - VOUS AVEZ PERDU"

    #Contrôle fin de jeu
    def controle_fin_jeu(self):
        nombre_mains = len(self.partie.joueur) #gérer multiple mains du Split
        valeur_croupier = self.partie.compteur.valeur_croupier

       #Fin jeu Comparaison finale tous les tours finis
        if self.stand_croupier and self.tour_joueur_fini:
            print("[DEBUG] Comparaison finale lancée !")
            self.jeu_fini = True

            if nombre_mains == 1:
                valeur_main = self.partie.compteur.valeur_joueur[0]

                if valeur_croupier > 21:
                    self.message_jeu_fini = "Le croupier a dépassé 21 - VOUS AVEZ GAGNÉ"
                elif valeur_croupier == 21 and valeur_main != 21:
                    self.message_jeu_fini = "Le croupier a 21 - VOUS AVEZ PERDU"
                elif valeur_main > 21:
                    self.message_jeu_fini = "Vous avez dépassé 21 - VOUS AVEZ PERDU "
                elif valeur_main > valeur_croupier:
                    self.message_jeu_fini = "Vous avez une meilleure main - VOUS AVEZ GAGNÉ"
                elif valeur_main < valeur_croupier:
                    self.message_jeu_fini = "Le croupier a une meilleur main - VOUS AVEZ PERDU"
                else:
                    self.message_jeu_fini = "ÉGALITÉ  avec le croupier"

                print(self.message_jeu_fini)

            # Correction: Comparer avec toutes les mains du joueur (Cas du Split)
            else:
                resultats = []
                for i in range(nombre_mains):
                    valeur_main = self.partie.compteur.valeur_joueur[i]

                    if valeur_main > 21:
                        resultats.append(f"MAIN {i+1} PERDUE")
                    elif valeur_croupier > 21 and valeur_main <= 21:
                        resultats.append(f"MAIN {i+1}: GAGNÉE")
                        print(self.message_jeu_fini)
                    elif valeur_main > valeur_croupier:
                        resultats.append(f"MAIN {i+1} GAGNÉE")
                    elif valeur_main < valeur_croupier:
                        resultats.append(f"MAIN {i+1} PERDUE")
                    else:
                        resultats.append(f"MAIN {i+1}: ÉGALITÉ")

                self.message_jeu_fini = "    |    ".join(resultats)
                print(self.message_jeu_fini)

            #Paiement mises
            self.regler_mises()
            return
        print("[DEBUG] Comparaison finale PAS lancée")

        #Logique pendant le jeu
        if self.tour_joueur_fini:
            return
        #Contrôle dépassement Index si Split
        if self.index_main_joueur >= nombre_mains:
            return
        valeur_main = self.partie.compteur.valeur_joueur[self.index_main_joueur]

        if valeur_main > 21:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier_fini = True
                self.jeu_fini = True
                self.message_jeu_fini = " Au dessus de 21 - VOUS AVEZ PERDU"
            else:
                self.index_main_joueur +=1
        elif valeur_main == 21:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier.en_cours = True
            else:
                self.index_main_joueur += 1
        # Cas : le joueur "Stand"
        elif self.stand_joueur:
            if self.index_main_joueur == nombre_mains - 1:
                self.tour_joueur_fini = True
                self.tour_croupier.en_cours = True
            else:
                self.index_main_joueur += 1
                self.stand_joueur = False

        #Fallback gain mises
        if self.jeu_fini:
            self.regler_mises()
            return

        if self.tour_joueur_fini and not self.tour_croupier.en_cours:
            self.tour_croupier.demarrer()


    def regler_mises(self):
        valeur_croupier = self.partie.compteur.valeur_croupier
        for i, main in enumerate(self.partie.joueur):
            valeur_main = self.partie.compteur.valeur_joueur[i]
            mise = self.partie.mises[i]

            if valeur_croupier > 21:
                self.partie.solde += 2 * mise
            elif valeur_main == 21 and len(main) == 2 and valeur_croupier != 21:
                # Blackjack
                gain = mise * 2.5
                self.partie.solde += gain
            elif valeur_main > valeur_croupier:
                self.partie.solde += 2 * mise
            elif valeur_main == valeur_croupier:
                self.partie.solde += mise