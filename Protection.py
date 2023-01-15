#####
#Fichier contenant la classe Protection
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo : Améliorer le fonctionnement de la classe

#####

from Ship import cShip  
#import tkinter as tk
#mw=tk.Tk()
#canvas=tk.Canvas(mw,height=480,width=640, bg='black')

class cProtections():
    Compteur=0
    def __init__(self):
        cProtections.Compteur+=1
        self.__Compteur = cProtections.Compteur
        self.__amount = 4
        self.__x = 640 * self.Compteur/(cProtections.getAmount+1)
        self.__y = cShip.getShipY-35
        self.__width = cShip.getWidthS * 2 #largeur de la protection
        self.__height = 20 #hauteur de la protection 
        self.__durability = 10
        self.Apparence = canvas.create_rectangle(cProtections.getX, cProtections.getY, cProtections.getX + cProtections.getWidth, cProtections.getY + cProtections.getHeight,width=2,outline='black',fill='white')
        self.VieProtection = canvas.create_text(cProtections.getX + cProtections.getWidth/2, cProtections.getY + cProtections.getHeight/2,text=str(cProtections.getDurability),fill='red')

    def getCompteur(self):
        return self.__Compteur

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def getDurability(self):
        return self.__durability

    def getAmount(self):
        return self.__amount

    def setDurability(self):
        self.__durability -= 1 
        
    def Update(self):
        cProtections.setDurability(self)
        if cProtections.getDurability > 0:
            canvas.itemconfig(self.VieProtection,text=(str(cProtections.getDurability)))
        else:
            self.Destruction()
    
    def Destruction(self):
        canvas.delete(self.Apparence)
        canvas.delete(self.VieProtection)