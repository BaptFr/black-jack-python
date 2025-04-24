import tkinter as tk
from jeu.blackjack import Jeu, Paquet

root = tk.Tk()
root.title("BlackJack")
root.geometry("400x300")

jeu = Jeu()
paquet = Paquet()

# Tirage
   
carte = paquet.tirer() #class pour pop = tirer
jeu.joueur.append(carte)
carte = paquet.tirer()
jeu.croupier.append(carte)

carte = paquet.tirer() #class pour pop = tirer
jeu.joueur.append(carte)
carte = paquet.tirer()
jeu.croupier.append(carte)

#Affichage / style
label = tk.Label(root, text="BlackJack", font=("Arial", 24))
label.pack()

tk.Label(root, text=str(jeu.croupier[0]), bd="2", bg="lightgrey", font=("Arial", 16)).place(x=100, y=50)
tk.Label(root, text=str(jeu.croupier[0]), bd="2", bg="lightgrey", font=("Arial", 16)).place(x=150, y=50)
tk.Label(root, text=str(jeu.joueur[0]), font=("Arial", 16), fg="blue").place(x=100, y=200)
tk.Label(root, text=str(jeu.joueur[0]), font=("Arial", 16), fg="blue").place(x=150, y=200)

#test



print(jeu.joueur)
print(jeu.croupier)

root.mainloop()


