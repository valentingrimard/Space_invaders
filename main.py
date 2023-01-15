#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo : Régler le problème cannot import name 'cTir' from partially initialized module 'Tir' (most likely due to a circular import)
#       Problème créé car deux fonctions s'appellent entre elles 

#####


#Importation des modules nécessaires
from random import randint
import tkinter as tk 
from time import time

#Création de la fenêtre
mw=tk.Tk()

#Importation des classes 
from Ship import cShip
from Alien import cAlien
from Protection import cProtections
from Tir import cTir
from TirAlien import cTirAlien

#Définition des classes pour les utiliser 
Ship = cShip()
Alien = cAlien()
Protection = cProtections()


# Initialisation des variables
Score = 0
Ingame = False
GameLost = True
TimeShoot = 0


def Points(val):
    '''
    Fonction qui compte le score 
    '''
    global Score
    Score += val
    score.config(text='Score: '+str(Score))

def newGame():
    '''
    Fonction qui crée la partie
    Entrée : Rien
    Sortie : la liste : enemy
    '''
    global enemy
    canvas.grid()
    canvas.create_image(0,0,anchor='nw',image=imageBackground)
    winlose.grid_remove()
    BoutonJouer.grid_remove()
    cProtections.Compteur=0
    #protection = [cProtections() for i in range(4)]
    Ingame = True
    if GameLost:
        Vies = 100 
        Score = 0
        score.config(text='Score: '+str(Score))
    enemy=[]
    LifeDisplay(Vies)
    cAlien.compteur = 0
    for i in range(15):
        enemy.append(Alien())
    for i in enemy:
        i.cAlien.Create()
    MouvementAlien()
    Tir_Alien()
    return enemy

def Win():
    '''
    Fonction qui détecte si la partie est gagné
    '''
    global Ingame,GameLost
    win = True 
    for i in enemy:
        if i.vivant:
            win = False
    if win:
        canvas.grid_remove()
        winlose.config(text='Gagné !!')
        winlose.grid()
        canvas.delete("all")
        BoutonJouer.grid()
        BoutonJouer.config(text='Continuer')
        cAlien.setSpeedA = 0.5 
        Ingame = False
        DelTirs()
        GameLost = False


def Lose():
    '''
    Fonction qui détecte si la partie est perdue
    '''
    global Ingame,GameLost
    canvas.grid_remove()
    winlose.config(text='Perdu !!')
    winlose.grid()
    canvas.delete("all")
    BoutonJouer.grid()
    BoutonJouer.config(text='Rejouer')
    cAlien.setSpeedA = 0.5 
    Ingame = False
    DelTirs()
    GameLost = True

def MouvementAlien():
    '''
    Fonction qui permet aux aliens de se déplacer
    '''
    global enemy
    if Ingame:
        L=[i.vivant for i in enemy]
        if True in L:
            i=L.index(True)
            L.reverse()
            j=L.index(True)
            if (enemy[-j-1].cTirAlien.getX + cAlien.getWidthA >= 480 and cAlien.getDirA == 1) or (enemy[i].cTirAlien.getX - cAlien.getWidthA <= 0 and cAlien.getDirA == -1):
                cAlien.setDirA(-1)
                cAlien.setY(10)
                if cAlien.getY + cAlien.getHeightA/2 >= cProtections.getY:
                    GameLost()
            for i in enemy:
                i.x += cAlien.getSpeedA * cAlien.getDirA
                i.Affichage()  
            mw.after(5,MouvementAlien)

def DelTirs():
    '''
    Fonction qui supprime les tirs lorsqu'ils dépassent le cadre de l'écran
    '''
    for i in cTir.listeTirs:
        i.cTir.getTir = False
    for i in cTirAlien.listeTirsA:
        i.cTirAlien.getTirA = False

def Tir_Alien():
    '''
    Fonction qui génère les tirs des aliens aléatoirement
    '''
    global enemy
    if Ingame:
        L = [i.vivant for i in enemy]
        i = randint(0,len(enemy)-1)
        if L[i]:
            cTirAlien.listeTirsA.append(cTirAlien(i))
            mw.after(100,Tir_Alien)
        else:
            mw.after(1,Tir_Alien)

def LifeDisplay(life):
    '''
    Fonction qui affiche le nombre de vie 
    '''
    NbVies.config(text='Vies: '+str(life))

def Clavier(event):
    '''
    Fonction qui permet au joueur de se déplacer
    '''
    global TempsTir
    touche = event.keysym
    if touche == 'q' or touche == 'Left':
        cShip.deplacement(-1)
    elif touche == 'd' or touche == 'Right':
        cShip.deplacement(1)
    elif touche == 'space':
        TimeTir1 = time()
        if TimeTir1 - TimeShoot >= 1 or cTir.listeTirs == []:
            TimeShoot = TimeTir1
            Shoot = cTir()
            cTir.listeTirs.append(Shoot)
            cTir.listeTirs[cTir.Compteur-1].Deplacement()


imageShip = tk.PhotoImage(file='ship.gif')
imageAlien = tk.PhotoImage(file='enemy.gif')
imageBackground = tk.PhotoImage(file='ship.gif')

score = tk.Label(mw,text = 'Score: 0')
score.grid(row=1,column = 1)

NbVies = tk.Label(mw,text = "Vies: 3")
NbVies.grid(row=1,column = 2)

canvas=tk.Canvas(mw,height = 480,width = 640, bg = 'black')
canvas.grid(row = 2,column = 1,columnspan = 2)
canvas.grid_remove()
canvas.focus_set()
canvas.bind('<Key>',Clavier)

BoutonJouer=tk.Button(mw,text='Jouer',command=newGame)
BoutonJouer.grid(row=0,column=1)



BoutonQuitter=tk.Button(mw,text = 'Quitter',command = mw.destroy)
BoutonQuitter.grid(row = 0,column = 2)

winlose = tk.Label(mw,text='Gagné')
winlose.grid(row = 1,column = 0)
winlose.grid_remove()

mw.mainloop()
