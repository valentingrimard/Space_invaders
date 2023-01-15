#####
#Fichier contenant la classe Alien
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####

#import tkinter as tk 
#imageAlien = tk.PhotoImage(file='enemy.gif')
#mw=tk.Tk()
#canvas=tk.Canvas(mw,height=480,width=640, bg='black')

class cAlien():
    
    compteur=0
    def __init__(self):
        '''
        '''
        cAlien.compteur += 1
        self.__compteur = cAlien.Compteur
        self.__vivant = True
        self.__space = 10 # écart entre deux aliens
        self.__width = 22  # largeur de l'alien
        self.__x = self.compteur*(self.__space + self.__width)
        self.__y = 16 # hauteur de l'alien
        self.__dirA = 1
        self.__speedA = 0.5
        self.__acceleration = 0.05
    
    def getWidthA(self): #renvoie la largeur de l'alien
        return (self.__width)

    def getHeightA(self):#renvoie la hauteur de l'alien
        return (self.__y)

    def getX(self):
        return (self.__x)

    def getY(self):
        return (self.__y)

    def getAccel(self):
        return (self.__acceleration)

    def getCompteur(self):
        return (self.__compteur)   

    def getAlive(self):    #renvoie si l'alien est vivant ou non
        return (self.__vivant)

    def getDirA(self):
        return (self.__dirA)

    def setY(self,val):
        self.__y += val 

    def setDirA(self,val):
        self.__dirA = self.__dirA * val 

    def getSpeedA(self):
        return (self.__speedA)

    def setSpeedA(self,val):
        self.__speedA += val

    def Create(self):
        self.apparence = canvas.create_image(cAlien.getWidthA,cAlien.getHeightA,anchor='nw',image=imageAlien)

    def Affichage(self):
        canvas.coords(self.apparence,cAlien.getWidthA,cAlien.getHeightA)