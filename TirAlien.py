#####
#Fichier contenant la classe TirAlien
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo : ajouter l'image enemylaser pour les tirs des aliens

#####

#import tkinter as tk 
#imageTirAlien = tk.PhotoImage(file='enemylaser.gif')
#mw=tk.Tk()
#canvas=tk.Canvas(mw,height=480,width=640, bg='black')

from Ship import cShip
from main import newGame,Lose,LifeDisplay
from Protection import cProtections


class cTirAlien():
    '''
    '''
    listeTirsA = []
    def __init__(self,i):
        self.__x = newGame[i].cTirAlien.getX
        self.__y = newGame[i].cTirAlien.getY
        self.apparence = canvas.create_line(cTirAlien.getX , cTirAlien.getY-4 , cTirAlien.getX ,cTirAlien.getY , fill='white')
        self.__tirA = True
        self.__speedTirA = 0.5
        self.Deplacement()

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getTirA(self):
        return self.__tirA

    def getSpeedTirA(self):
        return self.__speedTirA

    def setTirA(self,val):
        self.__tirA = val

    def setY(self,valY):
        self.__y += valY

    def affichage(self):
        canvas.coords(self.apparence , cTirAlien.getX , cTirAlien.getY-4 , cTirAlien.getX , cTirAlien.getY)
        
    def Deplacement(self):
        if self.__tirA:
            cTirAlien.setY(self,cTirAlien.getSpeedTirA)
            self.affichage()
            self.FinTir()
            mw.after(5,self.Deplacement)
    
    def FinTir(self):
        global life
        if cTirAlien.getY > 480:
            cTirAlien.setTirA(self,False)
            canvas.delete(self.apparence)
            del cTirAlien.listeTirsA[0]
        elif cTirAlien.getY >= cShip.getShipY - 5 and cTirAlien.getY <= cShip.getShipY + 5 and cTirAlien.getX <= cShip.getShipX + cShip.getWidthS/2 and cTirAlien.getX >= cShip.getShipX - cShip.getWidthS/2 :
                cTirAlien.setTirA(self,False)
                canvas.delete(self.apparence)
                del cTirAlien.listeTirsA[0]
                life -= 1
                LifeDisplay(life)
                if life == 0:
                    Lose()
        else:
            var = [cProtections() for i in range(4)]
            for i in var:
                if i.cProtections.getDurability > 0 and cTirAlien.getX >= i.cTirAlien.getX and cTirAlien.getX <= i.cTirAlien.getX + cProtections.getWidth and cTirAlien.getY >= cProtections.getY and cTirAlien.getY <= cProtections.getY + cProtections.getHeight:
                    i.Update()
                    cTirAlien.setTirA(self,False)
                    canvas.delete(self.apparence)
                    del cTirAlien.listeTirsA[0]