import pygame
import os
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

solde_initial = 1000
gestion_partie = GestionPartie(solde_initial)

#TEST DE COMBINAISON 1ere main au lancement
# carte1 = Carte("4", "Coeur")
# carte2 = Carte("6", "Carreau")
# gestion_partie.partie.joueur = [[carte1, carte2]]
# gestion_partie.partie.compteur.mise_a_j_valeur_main(gestion_partie.partie)
jeu = None
controleur = None
tour_croupier = None
tour_joueur = None

# pygame config affichage
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" BLACKJACK ")
font = pygame.font.SysFont("Arial", 24)
background_image = pygame.image.load("assets/images/fond/background.png")
fond_image = pygame.transform.scale(background_image, screen.get_size())

images_cartes = {}

#Boutons mises avant début du jeu
saisie_mise_active = True
mise_choisie = 0
jeu_initialise = False
message_erreur_mise = False


mises_possibles = [25, 50, 100]
boutons_mises = [
    (Bouton(50, 300, 100, 40, "25 €", (26, 35, 126), (255, 255, 255), font), 25),
    (Bouton(160, 300, 100, 40, "50 €", (26, 35, 126), (255, 255, 255), font), 50),
    (Bouton(270, 300, 100, 40, "100 €", (26, 35, 126), (255, 255, 255), font), 100),
]
#Version dessinée bouton_lancer_partie = Bouton(400, 300, 200, 40, "Lancer la partie", (83, 109, 254), (255, 255, 255), font, visible=True)
bouton_lancer_partie = pygame.image.load("assets/images/boutons/lancer_partie_btn.png").convert_alpha()
position_bouton = (400, 290)
rect_bouton = bouton_lancer_partie.get_rect(topleft=position_bouton)

#clock framerate pour limiter
clock = pygame.time.Clock()
#images pour cartes
def charger_images_cartes():
    dossier = "assets/images/cartes"
    for fichier in os.listdir(dossier):
        if fichier.endswith(".png"):
            chemin = os.path.join(dossier, fichier)
            image = pygame.image.load(chemin).convert_alpha()
            # Redimensionne l'image
            image = pygame.transform.scale(image, (100, 140))
            images_cartes[fichier] = image
    chemin_dos = os.path.join(dossier, "back_card.png")
    if os.path.exists(chemin_dos):
        image_dos = pygame.image.load(chemin_dos).convert_alpha()
        image_dos = pygame.transform.scale(image_dos, (100, 140))
        images_cartes["dos"] = image_dos

#AFFICHAGE  style cartes / Fonction enum
def afficher_cartes(cartes, position_x_main, position_y_debut, masquee=False):
    espacement_vertical = 30
    for index_carte, carte in enumerate(cartes):
        position_y_carte = position_y_debut + index_carte * espacement_vertical
        #Décalage cartes
        decalage_x = 10 if index_carte > 0 else 0
        position_x_carte = position_x_main + decalage_x
        #Masque 2eme carte croupier
        if masquee and index_carte == 1:
            dos_image = images_cartes.get("dos")
            if dos_image:
                screen.blit(dos_image, (position_x_carte, position_y_carte))
        else:
            nom_image = os.path.basename(carte.image_path())
            image = images_cartes.get(nom_image)
            if image:
                screen.blit(image, (position_x_carte, position_y_carte))
            else:
                # fallback texte si image non trouvée
                texte = font.render(f"{carte.valeur} {carte.couleur}", True, (0, 0, 0))
                screen.blit(texte, (position_x_carte, position_y_carte))
charger_images_cartes()

def afficher_message_texte(message, x, y):
    texte = font.render(message, True, (211, 211, 211))
    screen.blit(texte, (x, y))

def afficher_mains_joueur(joueur):
    position_y_cartes = 375
    position_x_depart = 200
    espacement_y = 200  #Ecart pour split
    for index_main, main in enumerate(joueur):
        #Gestion affichage Split
        position_x_main = position_x_depart + index_main *espacement_y
        afficher_cartes(main, position_x_main, position_y_cartes)
        #Main active + visuel
        if index_main == controleur.index_main_joueur:
             pygame.draw.rect(
                screen,
                (255, 0, 0),
                (position_x_main -10, position_y_cartes, 140, 120 + 30 * len(main)),
                2
            )

def afficher_mises(mises):
    position_x = 50
    position_y = 320
    espacement = 250

    for i, mise in enumerate(mises):
        texte_mise = font.render(f"Mise main: {mise} €", True, (211, 211, 211))
        screen.blit(texte_mise, (position_x + i * espacement, position_y))

def afficher_message_mise():
        texte = font.render("Veuillez choisir une mise avant de commencer", True, (255, 0, 0))
        screen.blit(texte, (50, 250))

def afficher_solde(solde):
    texte_solde = font.render(f"Solde : {solde} €", True, (211, 211, 211))
    screen.blit(texte_solde, (600, 550))


def afficher_score_croupier_une_carte(partie, masquee):
        if masquee and len(partie.croupier) > 0:
            premiere_carte = partie.croupier[0]
            valeur_premiere_carte = jeu.compteur.valeurs_cartes[premiere_carte.valeur]
            return f"Croupier: {valeur_premiere_carte}"
        else:
            return f"Croupier: {jeu.compteur.valeur_croupier}"


## TEST TERMINAL  ##
if jeu and controleur:
    print(jeu.croupier)
    print("Masquée")
    print(jeu.joueur)
    print(jeu.compteur.valeur_joueur)


## GESTION PARAMETRES AFFICHAGE PYGAME ##
bouton_tirer = Bouton(600, 350, 100, 40, "Tirer", (24, 148, 48), (255, 255, 255), font, visible=False)
bouton_rester = Bouton(600, 400, 100, 40, "Rester", (200, 0, 0), (255, 255, 255), font,visible=False)
bouton_restart = Bouton(550, 350, 200, 80, "Rejouer", (0, 0, 200), (200, 200, 200), font, visible = False)
bouton_split =  Bouton(600, 450, 100, 40, "Split", (255, 215, 0), (255, 255, 255), font, visible=False)
bouton_doubler = Bouton(600, 500, 100, 40, "Doubler", (255, 165, 0), (255, 255, 255), font, visible=False)
#GESTION du rafraichissement: action/inaction
running = True
besoin_rafraichissement = True

#Index main joueur
if gestion_partie.controleur and gestion_partie.tour_croupier:
      if gestion_partie.tour_croupier.en_cours:
        gestion_partie.controleur.index_main_joueur = 0
else:
    print("Erreur :Tour corupier ou  controleur non initialisé.")

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

            #Clic Bouton Mises
            if saisie_mise_active:
                bouton_restart.visible = False
                for bouton, mise in boutons_mises:
                    if bouton.est_clique(pos):
                        solde_actuel = gestion_partie.partie.solde if gestion_partie.partie else gestion_partie.solde_initial
                        if mise_choisie + mise > solde_actuel  :
                            print(f"Solde insuffisant")
                        else:
                            mise_choisie += mise
                            print(f"Mise choisie : {mise_choisie} €")
                            besoin_rafraichissement = True
                        break
                # Récupération des objets après création de la partie
                if rect_bouton.collidepoint(pos):
                    if mise_choisie == 0:
                        message_erreur_mise = True
                        besoin_rafraichissement = True
                    else:
                        message_erreur_mise = False
                        saisie_mise_active = False
                        jeu_initialise = True
                        gestion_partie.nouvelle_partie(mise_initiale=mise_choisie)
                        jeu = gestion_partie.partie
                        controleur = gestion_partie.controleur
                        tour_croupier = gestion_partie.tour_croupier
                        tour_joueur = gestion_partie.tour_joueur
                        bouton_tirer.visible = True
                        bouton_rester.visible = True
                        besoin_rafraichissement = True
            else:
                #Clic Bouton SPLIT
                if bouton_split.visible and bouton_split.est_clique(pos) and not controleur.tour_joueur_fini:
                    tour_joueur.jouer("splitter", controleur.index_main_joueur)
                    besoin_rafraichissement = True

                #Clic Bouton DOUBLER
                elif bouton_doubler.visible and bouton_doubler.est_clique(pos) and not controleur.tour_joueur_fini:
                    tour_joueur.jouer("doubler", controleur.index_main_joueur)
                    besoin_rafraichissement = True

                #Clic bouton REJOUER
                elif controleur.jeu_fini and bouton_restart.est_clique(event.pos):
                    print("Nouvelle partie lancée")
                    print("Nouvelle mise attendue")
                    #Efface le dernier jeu
                    jeu = None
                    controleur = None
                    tour_joueur = None
                    tour_croupier = None
                    bouton_restart.visible = False
                    saisie_mise_active = True
                    jeu_initialise = False
                    mise_choisie = 0
                    besoin_rafraichissement = True

                #Clic Bouton TIRER
                elif bouton_tirer.est_clique(pos) and not controleur.tour_joueur_fini:
                    print("Carte tirée par le joueur")
                    controleur.tour_joueur.jouer("tirer")
                    jeu.compteur.mise_a_j_valeur_main(jeu)
                    controleur.controle_fin_jeu()
                    besoin_rafraichissement = True

                #Clic Bouton RESTER
                elif bouton_rester.est_clique(pos) and not controleur.tour_joueur_fini:
                    controleur.tour_joueur.jouer("stand")
                    besoin_rafraichissement = True


    if controleur is not None and controleur.tour_croupier.en_cours:
        controleur.tour_croupier.mise_a_jour()
        besoin_rafraichissement = True

    ##MAJ DE L'AFFICHAGE/Chaque action
    if besoin_rafraichissement:
        #Efface l'écran / fond
        screen.fill((50, 205, 50))
        #Background image
        screen.blit(background_image, (0,0))

        if gestion_partie.partie:
            afficher_solde(gestion_partie.partie.solde)
        else:
            afficher_solde(gestion_partie.solde_initial)

        #Aff Boutons Mises avant débit de partie
        if saisie_mise_active:
            for bouton, _ in boutons_mises:
                bouton.dessiner(screen)
            #bouton_lancer_partie.dessiner(screen)
            screen.blit(bouton_lancer_partie, position_bouton)

            texte_mise = font.render(f"Mise totale : {mise_choisie} €", True, (211, 211, 211))
            screen.blit(texte_mise, (50, 200))
            #Erreur si pas de mise
            if message_erreur_mise:
                afficher_message_mise()

        #Aff Cartes
        if jeu and controleur:
            afficher_cartes(jeu.croupier, 200, 50, masquee=not controleur.tour_joueur_fini)
            afficher_mains_joueur(jeu.joueur)

            #Aff Scores
            texte_compteur_joueur = font.render(f"Joueur: {jeu.compteur.valeur_joueur}", True,(211, 211, 211))
            texte_compteur_croupier = font.render(afficher_score_croupier_une_carte(jeu, masquee=not controleur.tour_joueur_fini), True, (211, 211, 211))
            screen.blit(texte_compteur_joueur, (50, 375))
            screen.blit(texte_compteur_croupier, (50, 50))

            #Mises & solde après début de partie
            afficher_mises(jeu.mises)

            #Gestion visibilité/condition boutons Splitter et Doubler
            index_valide = 0 <= controleur.index_main_joueur < len(jeu.joueur)
            bouton_split.visible = (
                index_valide and
                tour_joueur.peut_splitter(controleur.index_main_joueur) and
                not controleur.tour_joueur_fini and
                len(jeu.joueur) == 1
            )

            bouton_doubler.visible = (
                index_valide and
                tour_joueur.peut_doubler(controleur.index_main_joueur) and
                not controleur.tour_joueur_fini
            )

            #Fin: Messages + bouton restart
            if controleur.jeu_fini:
                message_fin = font.render(controleur.message_jeu_fini, True, (235, 237, 239), (52, 73, 94))
                screen.blit(message_fin, (240, 260))
                bouton_restart.visible = True
                bouton_tirer.visible = False
                bouton_rester.visible = False
            else:
                bouton_restart.visible = False
                bouton_tirer.visible = index_valide and not controleur.tour_joueur_fini
                bouton_rester.visible = index_valide and not controleur.tour_joueur_fini

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

