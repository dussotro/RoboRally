"""
Fichier de définition de classe

Classe à définir:
    - Robot
    - Plateau
    - Cartes
    - Joueur

Sous classe:
    - Plateau
        - vide
        - départ
        - arrivée
        - non vide
    - Cartes
        - avancer
        - reculer
        - tourner Gauche
        - tourner Droite
        - demi-tour
    - Joueur
        - utilisateur
        - IA
        
Propriété à ajouter:
    - Robot
        - Vie 
        - Direction
        - Position
    - Cartes
        - Priorite
        - Nb cases
        - Rotation

Actions à définir:
    - Robot
        - Turn
        - Forward ('+' ou '-')
    - Cartes
        - Selon la carte

"""


"""""""""""""""
Bibliothèque
"""""""""""""""
import random as rd
import numpy as np
        
"""""""""""""""
Variables
"""""""""""""""

"""""""""""""""
Classe
"""""""""""""""
class Robot(object):
    
    def __init__(self, sante_initiale, dir_initiale, abscisse, ordonee, plateau):
        self.vie = sante_initiale
        self.direction = dir_initiale
        self.__coords = [abscisse, ordonee] 
        self.plateau = plateau #on lie la map au robot pour faciliter l'utilisation et les mouvements
                
        
    def Turn(self, rotation):
        self.direction = (self.direction + rotation)%4 #tourner à droite ou à gauche

        
    def Forward(self, nbCase):
        if self.direction == 0:     #avancer vers la droite, reculer vers la gauche
            self.x += nbCase 
        elif self.direction == 2:   #avancer vers la gauche, reculer vers la droite
            self.x += -nbCase
        elif self.direction == 1:   #avancer vers le bas, reculer vers le haut
            self.y += -nbCase
        else:                       #avancer vers le haut, reculer vers le bas
            self.y += nbCase

    
    @property
    def x(self):
        return self.coords[0]

    @property
    def y(self):
        return self.coords[1]
    
    @property        
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, nouvCoord, plateau):
        x, y = nouvCoord
        x = max(0, x)
        x = min(plateau.maxMapx, x)
        y = max(0, y)
        y = min(plateau.maxMapy, y)
        self.__coords = (x, y)

        
                
        
#-----------------------------------------        
        
#définition des cartes à jouer
class Cartes(object):
    
    def __init__(self):
        self.priorite = 0
        self.rotation = 0
        self.nbCase = 0
        self.joueur = 0
        
 
 
class CarteAvancer(Cartes):
    
    def __init__(self):
        super.__init__()
        nombre = rd.randint(1,3)
        if nombre == 1:
            self.nbCase = 1
            self.priorite = 300
            
        elif nombre == 2:
            self.nbCase == 2
            self.priorite = 500
        else:
            self.nbCase == 3
            self.priorite = 700
        
class CarteReculer(Cartes):
    
    def __init__(self):
        super.__init__()
        self.priorite = 250
        self.nbCase = -1
    
class CarteTourner(Cartes):
    
    def __init__(self):
        super.__init__()
        self.priorite = 230
        nombre = rd.randint(1,2)
        if nombre == 1:
            self.rotation = 1 #rotation droite
        else:
            self.rotation = -1 #rotation gauche
        
    
class CarteDemiTour(Cartes):
    
    def __init__(self):
        super.__init__()
        self.priorite = 200
        self.rotation = 2        

#----------------------------------------------        
class Joueur(object):

    def __init__(self, plateau):        
        self.nbCartesDistribuees = 9
        self.nbCartesJouees = 5
        x, y = rd.randint(1, 4), rd.randint(1, 4)
        self.robot = Robot(9, 1, x, y, plateau)
        self.cartes = []
        #sante_initiale, dir_initiale, abscisse, ordonee, plateau    
        self.fil_rouge = [0] #ligne d'arrivée non franchie
        checkpoints = 0
        for i in plateau:
            for j in i:
                if ord(j) == 86 or ord(j) == 87:
                    checkpoints += 1
        self.fil_rouge += checkpoints * [0]
        
class Utilisateur(Joueur):

    def __init__(self, plateau):
        super.__init__(plateau)
        
class IA(Joueur):
    
    def __init__(self, plateau):
        super.__init__(plateau)















































