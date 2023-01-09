#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####

from tkinter import Tk, Label, Button, StringVar, Frame, Canvas
from Ship import cShip

class Affichage():
    """
    Classe permettant de créer le canvas
    """
    def __init__(self):
        """
        title : Titre de la fenêtre
        geometry : Taille de la fenêtre
        minsize et maxsize : En donnant la même valeur à minsize et maxsize on a une fenêtre qui ne peut pas être agrandie ni réduite à la main
        config : Permet de configurer la fenêtre, notamment la couleur du fond
        """
        self.window = Tk()
        self.window.title("Space Invaders")
        self.window.geometry("800x800")
        self.window.minsize(800, 800)
        self.window.maxsize(800, 800)
        self.window.config(background = "#FFFFFF")
        #self.create_menu_bar()

        #Crée la fenêtre initiale
        self.frame = Frame(self.window, bg = "#FFFFFF")
        self.frame.pack(expand = True)

        #Change le titre de la fenêtre
        self.label = Label(self.frame, text = "Space Invaders", font = ("Helvetica", 40), bg = "#FFFFFF")
        self.label.pack()

        #Crée le bouton JOUER
        self.button = Button(self.frame, text = "Jouer", font=("Helvetica", 20), bg = "#FFFFFF", command = self.play)
        self.button.pack(pady=20)

        #Crée le bouton QUITTER
        self.button = Button(self.frame, text = "Quitter", font=("Helvetica", 20), bg = "#FFFFFF", command = self.window.quit)
        self.button.pack(pady=20)

        #Crée le bouton A PROPOS 
        self.button = Button(self.frame, text = "A Propos", font=("Helvetica", 20), bg = "#FFFFFF", command = self.about)
        self.button.pack(pady=20)

    #Création du menu
    #def create_menu_bar(self):
    #    menu_bar = Menu(self)
    #    menu_game = Menu(menu_bar, tearoff = 0)
    #    menu_game.add_command(label = "Rejouer", command = self.play)
    #    menu_game.add_command(label = "Quitter", command = self.window.quit)
    #    menu_game.add_command(label = "A propos", command = self.about)

    #Création du "A propos"
    def about(self):
        self.button.destroy()
        self.button = Button(self.frame, text = "Jeu du Space Invaders \n Made by GRIMARD Valentin & SCHERDING Romain", font=("Helvetica", 20), bg = "#FFFFFF", command = self.button.destroy)
        self.button.pack()

    def play(self):
        """
        Fonction qui appelle la fonction create_dynamic_canvas lorsque l'utilisateur clique sur le bouton PLAY
        """
        #Détruit les fenêtres existantes et crée la fenêtre de jeu
        self.frame.destroy()
        self.frame = Frame(self.window, bg = "#FFFFFF")
        self.frame.pack(expand=True)

        #Crée la fenêtre dynamique dans laquelle on a le canvas (space invader)
        self.dynamicFrame = Frame(self.frame, bg = "#FFFFFF")
        self.create_dynamic_canvas()
        self.dynamicFrame.pack(expand = True, fill = "both")

        #Crée la zone de texte indiquant le score actuel
        self.score = StringVar()
        self.labelscore = Label(self.dynamicFrame, textvariable = self.score, font = ("Helvetica", 10), bg = "#FFFFFF")
        self.labelscore.pack()

    def create_dynamic_canvas(self):
        """
        Fonction qui crée le canvas, dans lequel on va retrouver le space invader
        """
        #Crée la fenêtre canvas de taille 800x600
        self.canvas = Canvas(self.dynamicFrame, width = 800, height = 600, bg = "#C8C8C8")
        self.canvas.pack()

        #Crée le bouton JOUER
        self.button = Button(self.frame, text = "Jouer", font = ("Helvetica", 20), bg = "#FFFFFF", command = self.play)
        self.button.pack(side = 'top' , padx = 20)

        #Crée le bouton QUITTER
        self.button = Button(self.frame, text = "Quitter", font = ("Helvetica", 20), bg = "#FFFFFF", command = self.window.quit)
        self.button.pack(side = 'top' , padx = 20)
        
        #Crée le vaisseau 
        self.canvas.create_oval(380,550,420,590,outline = 'black',fill = 'white')
        #    cShip.getShipX(self) - cShip.getShipR(self),
        #    cShip.getShipY(self) - cShip.getShipR(self),
        #    cShip.getShipX(self) + cShip.getShipR(self),
        #    cShip.getShipY(self) + cShip.getShipR(self),
        #    outline = 'black',fill = 'white')
        self.canvas.pack(side = 'bottom', expand = True)

        #Crée les aliens
        self.canvas.create_rectangle(20,20,80,60,outline = 'black', fill = 'blue')
        self.canvas.pack(side = 'top', expand = True)

    def move(self,event):
        key = event.keysym  # a la variable "touche" on associe un evenement du clavier 
        if key == 'Right':  # si on appuie sur fleche de droite
            if cShip.getShipX(self) < 780: # si le coté droit du vaissseau n'a pas atteint le bord droit de la fenetre 
                cShip.getShipX(self) += 9  # on décale la position du centre du vaisseau vers la droite
        if key == 'Left':  # si on appuie sur fleche de droite
            if cShip.getShipX(self) > 20:  # si le coté gauche du vaissseau n'a pas atteint le bord gauche de la fenetre 
                cShip.getShipX(self) -= 9  # on décale la position du centre du vaisseau vers la gauche
                
        self.canvas.coords(self.canvas.create_oval(380,550,420,590,outline = 'black',fill = 'white'),
        cShip.getShipX(self) - cShip.getShipR(self),
        cShip.getShipY(self) - cShip.getShipR(self),
        cShip.getShipX(self) + cShip.getShipR(self),
        cShip.getShipY(self) + cShip.getShipR(self))  # les coordonnes du vaisseau sont alors modifiées

    def move(self,event):
        key=event.keysym  # a la variable "touche" on associe un evenement du clavier 
        if key=='Right':  # si on appuie sur fleche de droite
            if cShip.getShipX(self) < 780: # si le coté droit du vaissseau n'a pas atteint le bord droit de la fenetre 
                cShip.getShipX(self) += 9  # on décale la position du centre du vaisseau vers la droite
        if key=='Left':  # si on appuie sur fleche de droite
            if cShip.getShipX(self) > 20:  # si le coté gauche du vaissseau n'a pas atteint le bord gauche de la fenetre 
                cShip.getShipX(self) -= 9  # on décale la position du centre du vaisseau vers la gauche
                
        self.canvas.coords(self.canvas.create_oval(380,550,420,590,outline = 'black',fill = 'white'),
        cShip.getShipX(self) - cShip.getShipR(self),
        cShip.getShipY(self) - cShip.getShipR(self),
        cShip.getShipX(self) + cShip.getShipR(self),
        cShip.getShipY(self) + cShip.getShipR(self))  # les coordonnes du vaisseau sont alors modifiées


app = Affichage()
app.window.mainloop()