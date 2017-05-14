# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:57:43 2017

@author: Romain
"""

"""""""""
Variables
"""""""""
murDroite = [38, 39, 40, 44, 45, 46, 48, 49, 53, 54, 55, 56, 57, 63, 64, 65, 67, 71, 72, 73, 74, 75, 76, 77, 85, 86, 87, 89, 93, 94, 95, 96, 97, 102, 103, 105]            
murGauche = [36, 41, 42, 44, 46, 47, 48, 49, 51, 58, 59, 60, 61, 63, 65, 66, 67, 69, 78, 79, 80, 81, 82, 83, 85, 87, 88, 89, 91, 98, 99, 100, 101, 103, 104, 105]
murHaut   = [35, 39, 42, 43, 45, 47, 48, 49, 50, 54, 55, 60, 61, 62, 64, 66, 67, 68, 72 ,73 ,74 ,81 ,82, 83, 84, 86, 88, 89 ,90 ,94 ,95 ,100, 101, 102, 104, 105]
murBas    = [37, 40, 41, 43, 45, 46, 47, 49, 52, 56, 57, 58, 59, 62, 64, 65, 66, 70, 75 ,76 ,77, 78, 79, 80, 84, 86, 87, 88, 92 ,96 ,97 ,98, 99, 102, 103, 104]

laser1D =   [53, 55, 56, 65, 74, 77]
laser1G =   [51, 59, 60, 63, 67, 80, 83]
laser1H =   [50, 54, 61, 64, 74, 83]
laser1B =   [52, 57, 58, 62, 66, 77, 80]

laser2D =   [71, 73, 75, 87]
laser2G =   [69, 79, 81, 85, 89]
laser2H =   [68, 72, 82, 86]
laser2B =   [70, 76, 78, 84, 88]

laser3D =   [93, 95, 96, 103]
laser3G =   [91, 99, 100, 105]
laser3H =   [90, 94, 101, 102]
laser3B =   [92, 97, 98, 104]

"""""""""
Classes
"""""""""
#définition du plateau
class Map(object):
    
    def __init__(self, fichier):
 
        note = open(fichier, "r")
        lignes = note.readlines()
        plateau = [list(i) for i in lignes]
        for i in plateau:
            i.pop(-1)
        self.maxMapx = len(plateau[0])
        self.maxMapy = len(plateau)      
        for i in plateau:
            for j in i:
                j = Case(j)
        self.map = plateau    
        note.close()
        self.spawn = [(1,1),(1,15),(9,1),(9,15)] #lieux d'apparition (possibles) initiaux des robots 
        self.IApos = []
        cases = []
        for i in plateau:
            for j in plateau[0]:
                cases.append(Case(j))
        self.cases = cases

    def __str__(self):
        return 'le plateau est \n {}'.format(self.map)
    




    
class Case(str):

    def __init__(self, lettre):
        self.murD = 0
        self.murG = 0
        self.murH = 0
        self.murB = 0
        self.laserD = 0
        self.laserG = 0
        self.laserH = 0
        self.laserB = 0
        self.trou = False
        self.check = 0
        self.depart = 0
        self.arrivee = 0
        
        
        if ord(self) == 34:
            self.trou = True
            
        if ord(self) in murDroite:
            self.murD = 1    
        if ord(self) in murGauche:
            self.murG = 1   
        if ord(self) in murHaut:
            self.murH = 1
        if ord(self) in murBas:
            self.murB = 1
        
        if ord(self) in laser1D:
            self.laserD = 1
        if ord(self) in laser1G:
            self.laserG = 1        
        if ord(self) in laser1H:
            self.laserH = 1        
        if ord(self) in laser1B:
            self.laserB = 1        
        
        if ord(self) in laser2D:
            self.laserD = 2
        if ord(self) in laser2G:
            self.laserG = 2
        if ord(self) in laser2H:
            self.laserH = 2
        if ord(self) in laser2B:
            self.laserB = 2
            
        if ord(self) in laser3D:
            self.laserD = 3            
        if ord(self) in laser3G:
            self.laserG = 3     
        if ord(self) in laser3H:
            self.laserH = 3     
        if ord(self) in laser3B:
            self.laserB = 3     
            
        if ord(self) == 106:
            self.depart = 1
        if ord(self) == 107:
            self.arrivee = 1
        if ord(self) == 108:
            self.check = 1
        if ord(self) == 109:
            self.check = 2
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
