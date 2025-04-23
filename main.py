import tkinter as tk
from jeu.blackjack import Jeu, Paquet

root = tk.Tk()
root.title("BlackJack")
root.geometry("400x300")

jeu = Jeu()
paquet = Paquet()
carte = paquet.tirer() #class pour pop = tirer

#test
label = tk.Label(root, text="BlackJack", font=("Arial", 24))
label.pack()

carte_label = tk.Label(root, text=str(carte), font=("Arial", 18))
carte_label.pack()

print(jeu.joueur)

root.mainloop()


