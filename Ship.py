#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####


class cShip():
    """
    Classe permettant de créer le vaisseau
    """
    def __init__(self,centreX,centreY,rayonS):
        self.__centreX = centreX  # centre du vaisseau en x (430)
        self.__centreY = centreY  # centre du vaisseau en y (470)
        self.__rayonS = rayonS    # rayon du vaisseau (15)
        

    def getShipX(self):
        return self.__centreX

    def getShipY(self):
        return self.__centreY

    def getShipR(self):
        return self.__rayonS