import pygame
pygame.init()

from jeu.tirage import Tirage
from jeu.cartes import Carte
from jeu.paquet import Paquet
from jeu.compteur import Compteur
from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.tour_joueur import TourJoueur
from jeu.gestion_partie import GestionPartie
from jeu.bouton import Bouton

gestion_partie = GestionPartie()
gestion_partie.nouvelle_partie()

carte1 = Carte("5", "Coeur")
carte2 = Carte("5", "Carreau")
gestion_partie.partie.joueur = [[carte1, carte2]]
gestion_partie.partie.compteur.mise_a_j_valeur_main(gestion_partie.partie)



jeu = gestion_partie.partie
controleur = gestion_partie.controleur
tour_croupier = gestion_partie.tour_croupier
tour_joueur = gestion_partie.tour_joueur

# pygame config affichage
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" BLACKJACK ")
font = pygame.font.SysFont("Arial", 24)


# maj compteur main
jeu.compteur.mise_a_j_valeur_main(jeu)

#AFFICHAGE  style cartes / Fonction enum
def afficher_cartes(cartes, y_position, masquee=False):
    for i, carte in enumerate(cartes):
    #masque 2eme carte croupier
        if masquee and i == 1:
            pygame.draw.rect(screen, (0, 0, 255), (200 + i*120, y_position, 72, 96))
        else:
            style = jeu.paquet.style_carte(carte) #recup style carte
            couleur_texte = pygame.Color(style["color"])
            texte = font.render(str(carte), True, couleur_texte)
            screen.blit(texte, (200 + i*120, y_position)) # i ajout décalage 2nde carte

def afficher_mains_joueur(joueur):
    y_base = 375
    espacement_y = 120
    for i, main in enumerate(joueur):
        afficher_cartes(main, y_base + i * espacement_y)

def afficher_score_croupier_une_carte(partie, masquee):
        if masquee and len(partie.croupier) > 0:
            premiere_carte = partie.croupier[0]
            valeur_premiere_carte = jeu.compteur.valeurs_cartes[premiere_carte.valeur]
            return f"Croupier: {valeur_premiere_carte}"
        else:
            return f"Croupier: {jeu.compteur.valeur_croupier}"




## TEST TERMINAL  ##
print(jeu.croupier)
print("Masquée")
print(jeu.joueur)
print(jeu.compteur.valeur_joueur)


## GESTION PARAMETRES AFFICHAGE PYGAME ##
bouton_tirer = Bouton(600, 400, 100, 40, "Tirer", (24, 148, 48), (0, 0, 0), font, visible=True)
bouton_rester = Bouton(600, 450, 100, 40, "Rester", (200, 0, 0), (0, 0, 0), font,visible=True)
bouton_restart = Bouton(300, 480, 200, 80, "Rejouer", (0, 0, 200), (200, 200, 200), font, visible = False)
bouton_split =  Bouton(600, 500, 100, 40, "Split", (150, 150, 0), (0, 0, 0), font, visible=False)
bouton_doubler = Bouton(600, 650, 100, 40, "Doubler", (150, 150, 0), (0, 0, 0), font, visible=False)
#GESTION du rafraichissement: action/inaction
#clock framerate pour limiter
clock = pygame.time.Clock()
running = True
besoin_rafraichissement = True

#Index main joueur
controleur.index_main_joueur = 0

#méthode tirage carte avec index main
def tirer_carte_joueur_index(partie, index_main):
    carte = partie.paquet.tirer()
    partie.joueur[index_main].append(carte)
    partie.compteur.mise_a_j_valeur_main(partie)



#JEU ACTIF- cycle principal pygame
while running:
    ##GESTION D'EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            #Clic Bouton SPLIT
            if bouton_split.visible and bouton_split.est_clique(pos) and not controleur.tour_joueur_fini:
               tour_joueur.jouer("splitter", controleur.index_main_joueur)
               besoin_rafraichissement = True

            #Clic Bouton DOUBLER
            elif bouton_doubler.visible and bouton_doubler.est_clique(pos) and not controleur.tour_joueur_fini:
                main = jeu.joueur[controleur.index_main_joueur]
                valeur = jeu.compteur.calcul_valeur_main(main)
                if len(main) == 2 and valeur in [9, 10, 11]:
                    jeu.tirer_carte_joueur(controleur.index_main_joueur)
                    print("Doubler: tirage d'une seule carte")
                    controleur.tour_joueur_fini = True
                    besoin_rafraichissement = True

            #Clic bouton REJOUER
            elif controleur.jeu_fini and bouton_restart.est_clique(event.pos):
                print("Nouvelle partie lancée")
                gestion_partie.nouvelle_partie()
                jeu = gestion_partie.partie
                controleur = gestion_partie.controleur
                tour_croupier = gestion_partie.tour_croupier
                besoin_rafraichissement = True

            #Clic Bouton TIRER
            elif bouton_tirer.est_clique(pos) and not controleur.tour_joueur_fini:
                print("Carte tirée par le joueur")
                tirer_carte_joueur_index(jeu, controleur.index_main_joueur)
                jeu.compteur.mise_a_j_valeur_main(jeu)
                controleur.controle_fin_jeu()
                besoin_rafraichissement = True

            #Clic Bouton RESTER
            elif bouton_rester.est_clique(pos) and not controleur.tour_joueur_fini:
                print("Joueur reste / maintenant au croupier")
                controleur.tour_joueur_fini = True
                controleur.stand_joueur = True
                tour_croupier.demarrer()
                controleur.controle_fin_jeu()
                besoin_rafraichissement = True


    if tour_croupier.en_cours:
        tour_croupier.mise_a_jour()
        besoin_rafraichissement = True

    ##MAJ DE L'AFFICHAGE/Chaque action
    if besoin_rafraichissement:
        #Efface l'écran / fond
        screen.fill((50, 205, 50))


        #Cartes
        afficher_cartes(jeu.croupier, 50, masquee=not controleur.tour_joueur_fini)
        afficher_cartes(jeu.joueur[0], 375)

        #Scores
        texte_compteur_joueur = font.render(f"Joueur: {jeu.compteur.valeur_joueur}", True,(0, 0, 0))
        texte_compteur_croupier = font.render(afficher_score_croupier_une_carte(jeu, masquee=not controleur.tour_joueur_fini), True, (0, 0, 0))
        screen.blit(texte_compteur_joueur, (50, 375))
        screen.blit(texte_compteur_croupier, (50, 50))

         #Gestion visibilité/condition boutons Splitter et Doubler
        bouton_split.visible = tour_joueur.peut_splitter(controleur.index_main_joueur) and not controleur.tour_joueur_fini and len(jeu.joueur) == 1
        bouton_doubler.visible = tour_joueur.peut_doubler(controleur.index_main_joueur) and not controleur.tour_joueur_fini

        #Fin: Messages + bouton restart
        if controleur.jeu_fini:
            message_fin = font.render(controleur.message_jeu_fini, True, (200, 0, 0))
            screen.blit(message_fin, (100, 200))
            bouton_restart.visible = True
            bouton_tirer.visible = False
            bouton_rester.visible = False
        else:
            bouton_restart.visible = False
            bouton_tirer.visible = True
            bouton_rester.visible = True


        #Boutons
        bouton_tirer.dessiner(screen)
        bouton_rester.dessiner(screen)
        bouton_restart.dessiner(screen)
        bouton_split.dessiner(screen)
        bouton_doubler.dessiner(screen)
        # Màj affichage écran
        pygame.time.delay(700)
        pygame.display.flip()
        besoin_rafraichissement = False  #blocage rafraichissement inaction

        #Limite en FPS:
    clock.tick(2)

