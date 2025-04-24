import tkinter as tk
from jeu.blackjack import Jeu, Paquet

root = tk.Tk()
root.title("BlackJack")
root.geometry("400x300")

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



#Affichage / style
label = tk.Label(root, text="BlackJack", font=("Arial", 24))
label.pack()

#Affichage cartes joueur/croupier / Fonction enum

for i, carte in enumerate(jeu.joueur):
    style = paquet.style_carte(carte)
    tk.Label(root, text=str(carte), bd="2", font=style["font"], fg=style["fg"]).place(x=100 + i*100, y=50)  # i ajout décalage 2nde carte

for i, carte in enumerate(jeu.croupier):
    style = paquet.style_carte(carte)
    tk.Label(root, text=str(carte), bd="2", font=style["font"], fg=style["fg"]).place(x=100 + i*100, y=200)


# tk.Label(root, text=str(jeu.croupier[0]), bd="2", font=("Arial", 16)).place(x=100, y=50)
# tk.Label(root, text=str(jeu.croupier[1]), bd="2", font=("Arial", 16)).place(x=150, y=50)


# tk.Label(root, text=str(jeu.joueur[1]), bd="2", font=("Arial", 16)).place(x=150, y=200)

#test



print(jeu.joueur)
print(jeu.croupier)

root.mainloop()


