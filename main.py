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

# Tirage  /class pour pop = tirer

# #Tirage une carte joueur
# carte = paquet.tirer()
# style = paquet.style_carte(carte)
# jeu.joueur.append(carte)

# #Tirage une carte croupier
# carte = paquet.tirer()
# style = paquet.style_carte(carte)
# jeu.croupier.append(carte)

# #Tirage 2nde carte joueur
# carte = paquet.tirer()
# style = paquet.style_carte(carte)
# jeu.joueur.append(carte)

# #Tirage 2eme carte croupier
# carte = paquet.tirer()
# style = paquet.style_carte(carte)
# jeu.croupier.append(carte)


#Tirage amélioré en boucle
for _ in range (2):
    carte_joueur = paquet.tirer()
    jeu.joueur.append(carte_joueur)

    carte_croupier = paquet.tirer()
    jeu.croupier.append(carte_croupier)

#Affichage style cartes / Fonction enum
def afficher_cartes(cartes, y_position):
    for i, carte in enumerate(cartes):
        style = paquet.style_carte(carte) #recup style carte
        couleur_texte = pygame.Color(style["color"])
        texte = font.render(str(carte), True, couleur_texte)
        screen.blit(texte, (300 + i*140, y_position)) # i ajout décalage 2nde carte

#GESTION AFFICHAGE
#clock framerate pour limiter
clock = pygame.time.Clock()
running = True

#Jeu actif - cycle principal pygame
while running:
    #Effacer écran
    screen.fill((255, 255, 255))
    #Affichage position cartes croupier
    afficher_cartes(jeu.croupier, 50)
    #Affichage position cartes joueur
    afficher_cartes(jeu.joueur, 375)

    # Màj affichage écran
    pygame.display.flip()

    #gestionnaire d'évenement
    for event in pygame.event.get():
        #SI fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
    #Limite en FPS:
    clock.tick(60)

print(jeu.joueur)
print(jeu.croupier)