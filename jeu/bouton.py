import pygame

class Bouton:
    def __init__(self, x, y, width, height, texte, couleur_fond, couleur_texte, font, *, visible=True):
        self.rect = pygame.Rect(x, y, width, height)
        self.texte = texte
        self.couleur_fond = couleur_fond
        self.couleur_texte = couleur_texte
        self.font = font
        self.visible = visible

    def dessiner(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.couleur_fond, self.rect)
            texte_surface = self.font.render(self.texte, True, self.couleur_texte)
            text_rect = texte_surface.get_rect(center=self.rect.center)
            surface.blit(texte_surface, text_rect)

    def est_clique(self, pos_souris):
        return self.visible and self.rect.collidepoint(pos_souris)

    def afficher(self):
        self.visible = True

    def masquer(self):
        self.visible = False