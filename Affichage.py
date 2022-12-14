#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####

#from shutil import move
from random import randint
from tkinter import Tk, Label, Button, StringVar, Frame, Canvas
from Ship import cShip
from Alien import cAlien
from Protection import cProtection
#from Space_Invaders import deplacement
Ship = cShip()
Alien = cAlien()
Protection = cProtection()

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
        self.button = Button(
            self.frame,
            text = "Jeu du Space Invaders \n Made by GRIMARD Valentin & SCHERDING Romain",
            font=("Helvetica", 20),
            bg = "#FFFFFF",
            command = self.button.destroy)
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

    def deplacement(self,event):
        key = event.keysym            # à la variable "key" on associe un évènement du clavier 
        if key == 'Right':            # si on appuie sur la flèche de droite
            if Ship.getShipX() < 780: # si le coté droit du vaissseau n'a pas atteint le bord droit de la fenetre 
                Ship.setShipX(9)      # on décale la position du centre du vaisseau vers la droite
        if key == 'Left':             # si on appuie sur la flèche de gauche
            if Ship.getShipX() > 20:  # si le coté gauche du vaissseau n'a pas atteint le bord gauche de la fenetre 
                Ship.setShipX(-9)     # on décale la position du centre du vaisseau vers la gauche
                    
        self.canvas.coords(self.canvas.create_oval(
        Ship.getShipX() - Ship.getShipR(),
        Ship.getShipY() - Ship.getShipR(),
        Ship.getShipX() + Ship.getShipR(),
        Ship.getShipY() + Ship.getShipR(),
        outline = 'black',
        fill = 'white'))  # les coordonnées du vaisseau sont alors modifiées 

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
        

    def Ship(self):   
        #Crée le vaisseau 
        self.canvas.create_oval(
            Ship.getShipX() - Ship.getShipR(),
            Ship.getShipY() - Ship.getShipR(),
            Ship.getShipX() + Ship.getShipR(),
            Ship.getShipY() + Ship.getShipR(),
            outline = 'black',fill = 'green')
        self.canvas.pack(side = 'bottom', expand = True)
        #self.canvas.bind("<Key>",Affichage.deplacement())

    #Crée les groupes d'aliens
    def GroupeAlien(self):
        global groupeAlien
        listeAX = [0] #Liste des coordonnées du groupe d'alien en X
        listeAY = [0] #Liste des coordonnées du groupe d'alien en Y
        groupeAlien = []
        for i in range(1,5):
            for j in range(1,4):
                listeAX[-1] = 20+(Alien.getWidthA()+20)*(i-1)
                listeAY[-1] = 20+(Alien.getHeightA()+20)*(j-1)
                groupeAlien.append(self.canvas.create_rectangle(
                    listeAX[-1],
                    listeAY[-1],
                    listeAX[-1]+Alien.getWidthA(),
                    listeAY[-1]+Alien.getHeightA(),
                    outline = 'black',
                    fill = 'blue'))
                self.canvas.pack(side = 'top', expand = True)

    #Déplacement des aliens

    #Tir des aliens
    def TirAliens(self,dy,speed):
        global groupeAlien,MissileAlien
        if randint(0,2) == 0:
            groupeAlien = [ligne for ligne in groupeAlien if ligne]
            alien_aleatoire = randint(0,len(groupeAlien))
                
            PosXalien0,PosYalien0,PosXalien1,PosYalien1 = self.canvas.coords(groupeAlien[alien_aleatoire])
            MissileAlien = self.canvas.create_oval(
                (PosXalien0+25)-5,
                PosYalien0-5,
                (PosXalien0+25)+5,
                PosYalien0+5,
                outline='black',
                fill='yellow')
            #updateTirAliens()
        self.canvas.after(700, Affichage.TirAliens(self,-5,20))
    
    #Met à jour les tirs des aliens
    def updateTirAliens(self):
        global MissileAlien,groupeProtection
        VarMa=10
        Xma,Yma, Xmax, Ymay = self.canvas.coords(MissileAlien)
        if Yma > 600:
            self.canvas.delete(MissileAlien)
        else :
            for bloc in groupeProtection:
                [Xb0,Yb0,Xb1,Yb1]= self.canvas.coords(bloc)  
                if (Xb0)<(Xma)<(Xb1) and (Yb0)<(Yma)<(Yb1):
                    print (Yb0)                
                    self.canvas.delete(MissileAlien)
                    self.canvas.delete(bloc)
                    groupeProtection.remove(bloc)
                
            self.canvas.move(MissileAlien,0,VarMa)
            self.canvas.after(15,Affichage.updateTirAliens(self)) # on rappelle la fonction updateTirAliens après 15ms

    #Crée les protections 
    def Protection(self):
        global groupeProtection
        listePX = [0] #Liste des coordonnées des protections en X
        listePY = [0] #Liste des coordonnées des protections en Y
        groupeProtection = []
        for i in range(1,15):
            for j in range(1,4):
                listePX[-1] = 20+(Protection.getWidthA()+45)*(i-1)
                listePY[-1] = 400+(Protection.getHeightA())*(j-1)
                groupeProtection.append(self.canvas.create_rectangle(
                    listePX[-1],
                    listePY[-1],
                    listePX[-1]+Protection.getWidthA(),
                    listePY[-1]+Protection.getHeightA(),
                    outline = 'black',
                    fill = 'grey'))
        self.canvas.pack(side = 'bottom', expand = True)



app = Affichage()
app.window.mainloop()