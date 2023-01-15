#####
#Fichier contenant la classe Ship
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####

#import tkinter as tk 
#imageShip = tk.PhotoImage(file='ship.gif')
#mw=tk.Tk()
#canvas=tk.Canvas(mw,height=480,width=640, bg='black')


class cShip():
    
    def __init__(self):
        '''
        '''
        
        self.__width = 30 #largeur ship 
        self.__height = 32 #hauteur ship
        self.__x = 320
        self.__y = 443 
        self.__speed = 10 
        self.apparence = canvas.create_image(cShip.getShipX,cShip.getShipY,anchor='center',image=imageShip)

    def getShipX(self):
        return self.__x

    def getShipY(self):
        return self.__y
    
    def getWidthS(self):
        return self.__width

    def getHeightS(self):
        return self.__height  

    def getSpeedS(self):
        return self.__speed

    def setShipX(self,valX):
        self.__x += valX

    def setShipY(self,valY):
        self.__y += valY

    def deplacement(self,dir):
        if cShip.getShipX >= cShip.getWidthS and dir == -1:
            valX = cShip.getSpeedS * dir
            cShip.setShipX(self,valX)
        elif cShip.getShipX <= 480 - cShip.getWidthS and dir == 1: # 480 est la largeur du canvas
            valX = cShip.getSpeedS * dir
            cShip.setShipX(self,valX)
        self.Affichage()
        
    def Affichage(self):
        canvas.coords(self.apparence,cShip.getShipX,cShip.getShipY)
        
        
        