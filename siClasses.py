#####
#Fichier contenant les classes et le canvas
#Date de création : 05/12/2022
#Made By Valentin Grimard & Romain Scherding

#ToDo :

#####

import tkinter as tk

#class Alien:
#    """
#    """
#    def __init__(self):

#class Vaisseau:
#    """
#    """
#    def __init__(self):

#class Collisions:
#    """
#    """
#    def __init__(self):

class Screen:
    """
    Classe permettant de créer le canvas
    """
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Space Invaders")
        self.window.geometry("800x800")
        self.window.minsize(800, 800)
        self.window.maxsize(800, 800)
        self.window.config(background="#FFFFFF")

        self.frame = tk.Frame(self.window, bg="#FFFFFF")
        self.frame.pack(expand=True)

        self.label = tk.Label(self.frame, text="Space Invaders", font=("Helvetica", 40), bg="#FFFFFF")
        self.label.pack()

        self.button = tk.Button(self.frame, text="Jouer", font=("Helvetica", 20), bg="#FFFFFF", command=self.play)
        self.button.pack(pady=20)

        self.button = tk.Button(self.frame, text="Quitter", font=("Helvetica", 20), bg="#FFFFFF", command=self.window.quit)
        self.button.pack(pady=20)

    def play(self):
        """
        """
        self.frame.destroy()
        self.frame = tk.Frame(self.window, bg="#FFFFFF")
        self.frame.pack(expand=True)

        self.dynamicFrame = tk.Frame(self.frame, bg="#FFFFFF")
        self.create_dynamic_canvas()
        self.dynamicFrame.pack(expand="YES", fill="both")

    def create_dynamic_canvas(self):
        """
        """
        self.canvas = tk.Canvas(self.dynamicFrame, width=800, height=600, bg="#C8C8C8")
        self.canvas.pack()

app = Screen()
app.window.mainloop()

