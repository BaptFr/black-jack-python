import pygame
pygame.init()
import sys
from jeu.blackjack import Jeu, Paquet

# pygame config
screen= pygame.display.set_mode((800, 600))
pygame.display.set_caption(" BLACKJACK ")
font = pygame.font.SysFont("Arial", 24)

jeu = Jeu()
jeu_fini = False
message_fin_tour = ""



## TIRAGE DES CARTES ##
    # Ordre joueur -> croupier (x2)
for _ in range (2):
    carte_joueur = jeu.paquet.tirer()
    jeu.joueur.append(carte_joueur)

    carte_croupier = jeu.paquet.tirer()
    jeu.croupier.append(carte_croupier)


# maj compteur main
jeu.compteur.mise_a_j_valeur_main(jeu)
#vérif scores joueur/croupier
verif_blackjack = jeu.compteur.verification_black_jack(jeu)

if verif_blackjack == "blackjack_egalité":
    jeu_fini = True
    message_fin_tour = "ÉGALITÉ"
elif verif_blackjack == "blackjack_joueur":
    jeu_fini = True
    message_fin_tour = "BLACKJACK Félicitations vous avez gagné !"
elif verif_blackjack == "blackjack_croupier":
    jeu_fini = True
    message_fin_tour = "BLACKJACK croupier - Vous avez perdu"





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


def afficher_score_croupier_une_carte(jeu, masquee):
        if masquee and len(jeu.croupier) > 0:
            premiere_carte = jeu.croupier[0]
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
    # GESTION du rafraichissement: action/inaction
besoin_rafraichissement = True

    #clock framerate pour limiter
clock = pygame.time.Clock()
running = True

    #Jeu actif - cycle principal pygame
while running:
    #Effacer écran
    screen.fill((255, 255, 255))

    #Boutons d'actions rectangle
    bouton_tirer = pygame.Rect(600, 400, 100, 40)
    bouton_rester = pygame.Rect(600, 450, 100, 40)

    if besoin_rafraichissement:
        #Affichage f position cartes croupier et joueur | Boolean masquee pour la condition
        afficher_cartes(jeu.croupier, 50, masquee=True)
        afficher_cartes(jeu.joueur, 375)

        texte_compteur_joueur = font.render(f"Joueur: {jeu.compteur.valeur_joueur}", True,(0, 0, 0))
        texte_compteur_croupier = font.render(afficher_score_croupier_une_carte(jeu, masquee=True), True, (0, 0, 0))
        screen.blit(texte_compteur_joueur, (50, 375))
        screen.blit(texte_compteur_croupier, (50, 50))

        pygame.draw.rect(screen, (0, 200, 0), bouton_tirer)
        pygame.draw.rect(screen, (200, 0, 0), bouton_rester)
        texte_tirer = font.render("Tirer", True, (0, 0, 0))
        texte_rester = font.render("Rester", True, (0, 0, 0))
        screen.blit(texte_tirer, (bouton_tirer.x + 25, bouton_tirer.y + 5))
        screen.blit(texte_rester, (bouton_rester.x + 25, bouton_rester.y + 5))

        # Màj affichage écran
        pygame.display.flip()
        besoin_rafraichissement = False  #blocage rafraichissement inaction

    if jeu_fini:
        affichage_message_fin = font.render(message_fin_tour, True, (255, 0, 0))
        screen.blit(affichage_message_fin, (100, 300))

    ##GESTION D'EVENEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #SI tirage joueur
        elif event.type == pygame.MOUSEBUTTONDOWN:   #Clique dans la fenetre
            if bouton_tirer.collidepoint(event.pos):  # collidepoint() méthode, eventpos = coordonnées Si click dans le rectangle bouton tirer
                jeu.tirer_carte_joueur()
        besoin_rafraichissement = True

    #Limite en FPS:
    clock.tick(10)

