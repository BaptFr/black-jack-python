import pygame
pygame.init()
import sys
from jeu.blackjack import Jeu, Paquet

# pygame config
screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption(" BLACKJACK ")
font = pygame.font.SysFont("Arial", 24)

jeu = Jeu()
paquet = Paquet()

## TIRAGE DES CARTES ##
#Tirage en boucle. Ordre joueur -> croupier (x2)
for _ in range (2):
    carte_joueur = paquet.tirer()
    jeu.joueur.append(carte_joueur)

    carte_croupier = paquet.tirer()
    jeu.croupier.append(carte_croupier)

# affichage style cartes / Fonction enum
def afficher_cartes(cartes, y_position, masquee=False):
    for i, carte in enumerate(cartes):
        #conditions pour masquer 2eme carte croupier
        if masquee and i == 1:
            pygame.draw.rect(screen, (0, 0, 255), (300 + i*130, y_position, 72, 96))
        else:
            style = paquet.style_carte(carte) #recup style carte
            couleur_texte = pygame.Color(style["color"])
            texte = font.render(str(carte), True, couleur_texte)
            screen.blit(texte, (300 + i*130, y_position)) # i ajout décalage 2nde carte

# maj compteur main
jeu.compteur.mise_a_j_valeur_main(jeu)


## TEST TERMINAL  ##
print(jeu.croupier)
print(jeu.compteur.valeur_croupier)
print(jeu.joueur)
print(jeu.compteur.valeur_joueur)



## GESTION PARAMETRES AFFICHAGE PYGAME ##

# GESTION du rafraichissement: action/inaction
besoin_rafraichissement = True

#clock framerate pour limiter
clock = pygame.time.Clock()
running = True

#Jeu actif - cycle principal pygame
while running:
    #Effacer écran
    screen.fill((255, 255, 255))

    if besoin_rafraichissement:
        #Affichage f position cartes croupier et joueur | Boolean masquee pour la condition
        afficher_cartes(jeu.croupier, 50, masquee=True)
        afficher_cartes(jeu.joueur, 375)

        #Affichage de compturs
        texte_compteur_joueur = font.render(f"Joueur: {jeu.compteur.valeur_joueur}", True,(0, 0, 0))
        texte_compteur_croupier = font.render(f"Croupier: {jeu.compteur.valeur_croupier}", True,(0, 0, 0))
        screen.blit(texte_compteur_joueur, (50, 375))
        screen.blit(texte_compteur_croupier, (50, 50))

        # Màj affichage écran
        pygame.display.flip()
        besoin_rafraichissement = False  #blocage rafraichissement inaction


    #gestionnaire d'évenement  / fermeture fntre
    for event in pygame.event.get():
        #SI fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
    #Limite en FPS:
    clock.tick(10)

