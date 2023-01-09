#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####


class cProtection():
    """
    """
    def __init__(self):
        self.__width = 20  # largeur de la protection 
        self.__height = 10  # hauteur de la protection
        
    def getWidthA(self):
        return (self.__width)

    def getHeightA(self):
        return (self.__height)

    def setWidthA(self,width):
        self.__width = width

    def setShipY(self,height):
        self.__height = height