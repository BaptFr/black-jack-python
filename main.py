import pygame
pygame.init()
import sys

from jeu.tirage import Tirage
from jeu.cartes import Carte
from jeu.paquet import Paquet
from jeu.compteur import Compteur
from jeu.controleur import Controleur
from jeu.tour_croupier import TourCroupier
from jeu.gestion_partie import GestionPartie
from jeu.bouton import Bouton

gestion_partie = GestionPartie()
gestion_partie.nouvelle_partie()
jeu = gestion_partie.partie
controleur = gestion_partie.controleur
tour_croupier = gestion_partie.tour_croupier


# pygame config affichage
screen= pygame.display.set_mode((800, 600))
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
bouton_tirer = Bouton(600, 400, 100, 40, "Tirer", (0, 200, 0), (0, 0, 0), font, visible=True)
bouton_rester = Bouton(600, 450, 100, 40, "Rester", (200, 0, 0), (0, 0, 0), font,visible=True)
bouton_restart = Bouton(300, 480, 200, 80, "Rejouer", (0, 0, 200), (200, 200, 200), font, visible = False)

#GESTION du rafraichissement: action/inaction
#clock framerate pour limiter
clock = pygame.time.Clock()
running = True
besoin_rafraichissement = True

#Jeu actif - cycle principal pygame
while running:
    ##GESTION D'EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if controleur.jeu_fini and bouton_restart.est_clique(event.pos):
                print("Nouvelle partie lancée")
                gestion_partie.nouvelle_partie()
                jeu = gestion_partie.partie
                controleur = gestion_partie.controleur
                tour_croupier = gestion_partie.tour_croupier
                besoin_rafraichissement = True

            elif not controleur.tour_joueur_fini:
                if bouton_tirer.est_clique(event.pos) and not controleur.tour_joueur_fini:  # collidepoint() méthode, eventpos = coordonnées Si click dans le rectangle bouton tirer
                    jeu.tirer_carte_joueur()
                    print("joueur tire une carte")
                    controleur.controle_fin_jeu()
                    besoin_rafraichissement = True
                elif bouton_rester.est_clique(event.pos) and not controleur.tour_joueur_fini:
                    controleur.tour_joueur_fini = True
                    controleur.stand_joueur =True
                    controleur.controle_fin_jeu()
                    print("joueur reste / maintenant au croupier")
                    tour_croupier.action_croupier_etape()
                    besoin_rafraichissement = True
                elif controleur.tour_joueur_fini and controleur.tour_croupier_fini:
                    controleur.controle_fin_jeu()

    ##MAJ DE L'AFFICHAGE/Chaque action
    if besoin_rafraichissement:
        #Efface l'écran
        screen.fill((255, 255, 255))

        #Cartes
        afficher_cartes(jeu.croupier, 50, masquee=not controleur.tour_joueur_fini)
        afficher_cartes(jeu.joueur, 375)

        #Scores
        texte_compteur_joueur = font.render(f"Joueur: {jeu.compteur.valeur_joueur}", True,(0, 0, 0))
        texte_compteur_croupier = font.render(afficher_score_croupier_une_carte(jeu, masquee=not controleur.tour_joueur_fini), True, (0, 0, 0))
        screen.blit(texte_compteur_joueur, (50, 375))
        screen.blit(texte_compteur_croupier, (50, 50))

        controleur.controle_fin_jeu()
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
        # Màj affichage écran
        pygame.display.flip()
        besoin_rafraichissement = False  #blocage rafraichissement inaction

        #Limite en FPS:
    clock.tick(10)

