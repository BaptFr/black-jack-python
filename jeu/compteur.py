class Compteur:
    def __init__(self):
        self.valeur_joueur= 0
        self.valeur_croupier = 0
        self.valeurs_cartes = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "V": 10, "D": 10, "R": 10, "As": 11
        }

    def calcul_valeur_main(self, main, is_croupier=False):
        total_main = 0
        nombre_as = 0

        for carte in main:
            #d'abord reprendre valeur (string)
            valeur = carte.valeur
            #utiliser la conversion en int
            total_main += self.valeurs_cartes[valeur]
            #Gestion des As
            if valeur == "As":
                nombre_as +=1

        #Cas croupier
        if is_croupier:
            # Règle français "Soft 17"
            if 17 >=  total_main <=21 and nombre_as > 0:
               return total_main
            while total_main > 21 and nombre_as > 0:
                total_main -= 10
                nombre_as -=1
            return total_main

        #Cas joueur
        while total_main > 21 and nombre_as > 0:
                total_main -= 10
                nombre_as -=1

        return total_main

    def mise_a_j_valeur_main(self, partie):
        self.valeur_joueur = self.calcul_valeur_main(partie.joueur, is_croupier=False)
        self.valeur_croupier = self.calcul_valeur_main(partie.croupier, is_croupier=True)


