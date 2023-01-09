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
    def __init__(self):
        self.__centreX = 400  # centre du vaisseau en x 
        self.__centreY = 570  # centre du vaisseau en y 
        self.__rayonS = 20    # rayon du vaisseau 
        
    def getShipX(self):
        return self.__centreX

    def getShipY(self):
        return self.__centreY

    def getShipR(self):
        return self.__rayonS
