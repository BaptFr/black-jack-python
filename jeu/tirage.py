from .paquet import Paquet
from .compteur import Compteur



class Tirage:
    def __init__(self):
        #liste de mains
        self.joueur = [[]]
        self.croupier = []
        self.compteur = Compteur()
        self.paquet = Paquet()

        for _ in range(2):
            self.tirer_carte_joueur()
            self.tirer_carte_croupier()

    def afficher_valeurs(self):
        print(f"Main Croupier: {self.compteur.valeur_croupier}")
        print(f"Main Joueur: {self.compteur.valeur_joueur}")

    def  tirer_carte_joueur(self, index_main=0):
        carte = self.paquet.tirer()
        self.joueur[index_main].append(carte)
        self.compteur.mise_a_j_valeur_main(self)

    def  tirer_carte_croupier(self):
        carte = self.paquet.tirer()
        self.croupier.append(carte)
        self.compteur.mise_a_j_valeur_main(self)

    #Doubler
    def peut_doubler(self):
        if  9 <= self.compteur.calcul_valeur_main(self.joueur) <= 11 :
            return  True
        return False

    def action_doubler(self, index_main=0):
        main = self.joueur[index_main]
        if not self.peut_doubler(main):
            return False
        self.tirer_carte_joueur(index_main)
        print("Doubler: tirage d'une seule carte")
        return True

    #Splitter
    def peut_splitter(self):
        main = self.joueur[0]
        return len(main) == 2 and main[0].valeur == main[1].valeur

    def action_splitter(self):
        if not self.peut_splitter():
            return False
        main_initiale = self.joueur[0]
        nouvelle_main_1 = [main_initiale[0]]
        nouvelle_main_2 = [main_initiale[1]]

        self.joueur = [nouvelle_main_1, nouvelle_main_2]
        self.compteur.mise_a_j_valeur_main(self)

        print("Splint effectué")
        return True

