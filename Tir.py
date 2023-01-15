#####
#Fichier contenant la classe Tir
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo : Ajouter l'image shiplaser comme projectile

#####

#import tkinter as tk 
#imageTir = tk.PhotoImage(file='shiplaser.gif')
#mw=tk.Tk()
#canvas=tk.Canvas(mw,height=480,width=640, bg='black')

from Ship import cShip
from Alien import cAlien
from main import newGame,Points,Win 

class cTir:
    '''
    '''
    listeTirs = []
    Compteur=0
    def __init__(self):
        self.__x = cShip.getShipX
        self.__y = cShip.getShipY
        self.apparence = canvas.create_line(cTir.getX ,cTir.getY-4 ,cTir.getX ,cTir.getX ,fill = 'white')
        self.__tir = True
        self.__speedTir = 1
        cTir.Compteur += 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getTir(self):
        return self.__tir

    def getSpeedTir(self):
        return self.__speedTir    
    
    def Affichage(self):
        canvas.coords(self.apparence , cTir.getX , cTir.getX-4 , cTir.getX , cTir.getX)

    def setY(self,valY):
        self.__y -= valY

    def setTir(self,val):
        self.__tir = val
    
    def Deplacement(self):
        if cTir.getTir:
            cTir.setY(self,cTir.getSpeedTir)
            self.Affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
      

    def FinTir(self):
        if cTir.getY < 0:
            cTir.setTir(self,False)
            canvas.delete(self.apparence)
            del cTir.listeTirs[0]
            cTir.Compteur -= 1
        else:
            for i in newGame:
                if i.cAlien.getAlive and cTir.getY >= i.y and cTir.getY <= i.cTir.getY + cAlien.getHeightA and cTir.getX <= i.cTir.getX + cAlien.getWidthA and cTir.getX >= i.cTir.getX:
                    self.Destruction()
                    canvas.delete(i.apparence)
                    i.vivant = False
                    cAlien.setSpeedA(self,cAlien.getAccel)
                    Points(30)
                    Win()


    def Destruction(self):
        self.encours = False
        canvas.delete(self.apparence)
        del cTir.listeTirs[0]
        cTir.Compteur-=1