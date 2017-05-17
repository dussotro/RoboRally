#coding:utf-8

import random
import operator
import time

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



#class Terrain():
#   def __init__(self,file_txt):
#        """Constructeur de la classe Terrain
#        Parametres
#        ----------
#        file_txt : fichier texte 
#            Sert de base pour notre terrain (les cases sont reperees par differents caracteres) 
#        """
#        self.file  = file_txt #fichier hebergeant le terrain
#        self.carte = self.load(self.file) #voir methode load de la classe 
#        self.constantmap = self.carte #constantmap est une image a l'instant 0 de notre carte, qui servira lors de l'utilisation de la methode check
#        self.width = len(self.carte[0]) #largeur du terrain
#        self.height = len(self.carte) #hauteur du terrain
#        self.spawn = [(1,1),(1,15),(9,1),(9,15)] #lieux d'apparition (possibles) initiaux des robots 
#        self.bot_pos = []
#        self.non_collidable=[' ','F','H','Z','Q','S','D','V','C','R'] #Caracteres representant les cases sur lesquels on peut marcher
#        self.collidable=['W','P','O','M','L','-','*','+','/','#','$','€','£'] #Caracteres representant les cases sur lesquels on ne peut pas marcher
#        self.special_collidable=['0','1','2','3','4','5','6','7','8','9'] #Caracteres representant les murs
#        self.load_Elements() #voir methode load_Elements de la classe Terrain
#        
#    def load(self,file):
#        """ methode de chargement du terrain de jeu
#        
#        Parametres
#        ----------
#        file : fichier texte
#            Fichier hebergeant le terrain de jeu sous forme de caracteres
#           
#        Returns
#        -------
#        terrain : type liste
#            terrain est une liste qui contient chaque case du plateau de jeu, ordonee precisement. 
#            exemple : terrain[0,0] est la case tout en haut à gauche
#                      terrain[i,j] est la case situee a la (i-1)ème ligne, (j-1)ème colonne
#        """
#        f=open(file)
#        terrain = [] #creation de notre liste (de listes)
#        for line in f:
#            L=[] #creation d'une liste qui represente une ligne de notre terrain
#            for el in line:
#                L.append(el)
#            L.remove('\n')
#            terrain.append(L)
#        return terrain
#        
#    def load_Elements(self):
#        """ Méthode permettant de recueillir dans des listes les coordonnées des différents éléments de terrain
#        Returns
#        -------
#        Aucun. Néanmoins, cette méthode crée des variables de classe qui regroupent par élément (tapis roulant haut, bas, laser, etc...) les coordonnées d'apparition
#        """
#        Holes=[] #trous
#        tapisH, tapisG, tapisD, tapisB = [],[],[],[] #tapis roulants
#        laserH, laserG, laserD, laserB = [],[],[],[] #lasers
#        turnC,turnA = [],[] #tourniquets 
#        for a,i in enumerate(self.carte) :
#            for s,l in enumerate(i):
#                if i[s] =='F':
#                    flag =(a,s)
#                if i[s] =='H':
#                    Holes.append((a,s))
#                if i[s] == 'Z':
#                    tapisH.append((a,s))
#                if i[s] == 'Q':
#                    tapisG.append((a,s))
#                if i[s] == 'S':
#                    tapisB.append((a,s))
#                if i[s] == 'D':
#                    tapisD.append((a,s))
#                if i[s] == 'P':
#                    laserH.append((a,s))
#                if i[s] == 'O':
#                    laserG.append((a,s))
#                if i[s] == 'M':
#                    laserB.append((a,s))
#                if i[s] == 'L':
#                    laserD.append((a,s))
#                if i[s] == 'V':
#                    turnC.append((a,s))
#                if i[s] == 'C':
#                    turnA.append((a,s))
#        self.holes = Holes
#        self.flag = flag
#        self.tapisG = tapisG
#        self.tapisD = tapisD
#       self.tapisH = tapisH
#       self.tapisB = tapisB
#        self.laserG = laserG
#        self.laserD = laserD
#        self.laserH = laserH
#        self.laserB = laserB
#        self.turnA = turnA
#        self.turnC = turnC
#        

        
#    def Render(self):
#        for i in self.carte:
#            line = '|'.join(i)
#            print(line)



class Map(object):
    
    def __init__(self, fichier):
 
        note = open(fichier, "r")
        lignes = note.readlines()
        plateau = [list(i) for i in lignes]
        for i in plateau:
            i.pop(-1)
        self.maxMapx = len(plateau[0])
        self.maxMapy = len(plateau)      
        for i, m in enumerate(plateau):
            for j, n in enumerate(m):
                k = Case(plateau[i][j])
                plateau[i][j] = k
                if k == 'k':
                    coordFin = [i,j]
        self.map = plateau
        self.mapInit = self.map
        note.close()
        self.spawn = [(1,1),(1,6),(9,1),(6,9)] #lieux d'apparition (possibles) initiaux des robots 
        self.IApos = []
        self.flag = coordFin


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

class Robot():
    
    def __init__(self,terrain,name):
        """ Constructeur de la classe Robot
        
        Parametres
        ----------
        terrain : fichier texte
            Terrain hebergeant la partie
        name : type str
            Nom du robot
        """
        self.name = name
        self.terrain = terrain
        self.rspawn =random.choice(self.terrain.spawn) 
        self.x = self.rspawn[0]
        self.y = self.rspawn[1]
        self.coords = [self.x, self.y]
        self.dir = random.choice([0,1,2,3])
        self.__dicoDir = {3:'North',0:'East',1:'South',2:'West'}
        self.base = terrain.map
        self.__boundary = (terrain.maxMapy,terrain.maxMapx)
        self.life = 9
        self.win = False
        self.MAJ()
       
    

        
    def Turn(self, rotation):
        print('tourner')
        self.direction = (self.dir + rotation)%4 #tourner à droite ou à gauche
        self.MAJ()
        
    def Forward(self, nbCase, coord, plateau):
        print(plateau)
        for i in range(nbCase):
            if self.dir == 0 and plateau[coord[0]][coord[1]].murD == 0 and plateau[coord[0]+1][ coord[1]].murG == 0 and plateau[coord[0]][coord[1]].trou == False:     #avancer vers la droite, reculer vers la gauche
                self.x += 1
            elif self.dir == 2 and plateau[coord[0]][coord[1]].murG == 0 and plateau[coord[0] - 1][ coord[1]].murD == 0 and plateau[coord[0]][ coord[1]].trou == False:   #avancer vers la gauche, reculer vers la droite
                self.x += -1
            elif self.dir == 1 and plateau[coord[0]][coord[1]].murB == 0 and plateau[coord[0]][ coord[1] - 1].murH == 0 and plateau[coord[0]][coord[1]].trou == False:   #avancer vers le bas, reculer vers le haut
                self.y += -1
            elif self.dir == 3 and plateau[coord[0]][coord[1]].murH == 0 and plateau[coord[0]][ coord[1] + 1].murB == 0 and plateau[coord[0]][coord[1]].trou == False:                       #avancer vers le haut, reculer vers le bas
                self.y += 1
        self.MAJ()
    
    def Backward(self, coord, plateau):
        print(plateau)
        if self.dir == 0 and plateau[coord[0]][coord[1]].murG == 0 and plateau[coord[0] - 1][coord[1]].murD == 0:     #avancer vers la droite, reculer vers la gauche
            self.x += -1
        elif self.dir == 2 and plateau[coord[0]][coord[1]].murD == 0 and plateau[coord[0] + 1][coord[1]].murG == 0:   #avancer vers la gauche, reculer vers la droite
            self.x += 1
        elif self.dir == 1 and plateau[coord[0]][coord[1]].murH == 0 and plateau[coord[0]][coord[1] + 1].murB == 0:  #avancer vers le bas, reculer vers le haut
            self.y += 1
        elif self.dir == 3 and plateau[coord[0]][coord[1]].murB == 0 and plateau[coord[0]][coord[1] -1].murH == 0:    #avancer vers le haut, reculer vers le bas
            self.y += -1
        self.MAJ()
        
            
         
    def MAJ(self):
        """ Mise à jour des principaux éléments de jeu, notamment la position des 'R' sur le terrain
        """
        if self.x < self.terrain.maxMapx and self.y < self.terrain.maxMapy:
            self.terrain.map[self.x][self.y] = 'R'
            self.public_x,self.public_y = self.x,self.y
        else:
            self.__coordsRobot=self.rspawn
        print('dir : ' + self.__dicoDir[self.dir]) #affiche la direction dans laquelle se trouve le robot
        self.orientation = self.__dicoDir[self.dir]
        print(self.life) #affiche la vie actuelle du robot

        
    def handle_land(self):
        self.__coordsRobot = (self.x, self.y)
        """ Gestion du drapeau """
        if self.__coordsRobot == self.terrain.flag:
            self.win = True 
        """ Gestion des trous """
        if self.terrain.map[self.x][self.y]:
                self.__coordsRobot=self.rspawn
        """ Invariant """
        self.x,self.y =self.__coordsRobot
        self.MAJ()
 
    """ POUR LES 4 METHODES SUIVANTES :
        elles sont très similaires, seule la directon des lasers et l'orientation des murs change. 
        Ainsi la description ne sera faite qu'une seule fois
    """

    def check_up_laser(self):
        limit=[]
        exist = False
        damage = 0
        for i in range(self.terrain.maxMapy):
            for j in range(self.terrain.maxMapx):
                if ord(self.terrain.map[i][j])in (laser1H + laser2H + laser3H):
                    exist = True
                    if ord(self.terrain.map[i][j]) in laser1H:
                        damage = 1
                    elif ord(self.terrain.map[i][j]) in laser2H:
                        damage = 2
                    elif ord(self.terrain.map[i][j]) in laser3H:
                        damage = 3
                    limit.append(i)
        if exist :
            up_blocked = False
            limit = max(limit)
            for cases in range(self.y,limit):
                print("cases:" ,cases)    
                if self.terrain.map[self.x][cases].murB or self.terrain.map[self.x][cases].murH:
                    up_blocked = True
            if not up_blocked:
                print('merde ca marche pas')
                self.life-= damage
            if up_blocked and not(self.terrains.map[cases][self.y].murH):
                self.life-= damage

            
    def check_down_laser(self):
        limit=[]
        exist = False
        for i in range(self.terrain.maxMapy):
            for j in range(self.terrain.maxMapx):
                if ord(self.terrain.map[i][j])in (laser1B + laser2B + laser3B):
                    exist = True
                    if ord(self.terrain.map[i][j]) in laser1B:
                        damage = 1
                    elif ord(self.terrain.map[i][j]) in laser2B:
                        damage = 2
                    elif ord(self.terrain.map[i][j]) in laser3B:
                        damage = 3
                    limit.append(i)
        if exist :
            down_blocked = False
            limit = min(limit)
            for cases in range(self.y,limit):
                
                if self.terrain.map[self.x][cases].murH or self.terrain.map[self.x][cases].murB:
                    down_blocked = True
                print(down_blocked)
                    
            if not down_blocked:
                self.life-=damage
            if down_blocked and not(self.terrains.map[self.x][self.y].murB):
                self.life-=damage          

                
    def check_left_laser(self):
        limit=[]
        exist = False
        for i in range(self.terrain.maxMapy):
            for j in range(self.terrain.maxMapx):
                if ord(self.terrain.map[i][j])in (laser1G + laser2G + laser3G):
                    exist = True
                    if ord(self.terrain.map[i][j]) in laser1G:
                        damage = 1
                    elif ord(self.terrain.map[i][j]) in laser2G:
                        damage = 2
                    elif ord(self.terrain.map[i][j]) in laser3G:
                        damage = 3
                    limit.append(i)
        if exist :
            left_blocked = False
            limit = max(limit)
            for cases in range(self.y,limit,-1):
                print(cases)
                if self.terrain.map[cases][self.y].murD or self.terrain.map[cases][self.y].murG:
                    left_blocked = True
                   
            if not left_blocked:
                self.life-=damage
            if left_blocked and not(self.terrains.map[self.x][self.y].murG):
                self.life-=damage 

                
    def check_right_laser(self):
        limit=[]
        exist = False
        for i in range(self.terrain.maxMapy):
            for j in range(self.terrain.maxMapx):
                if ord(self.terrain.map[i][j])in (laser1H + laser2H + laser3H):
                    exist = True
                    if ord(self.terrain.map[i][j]) in laser1H:
                        damage = 1
                    elif ord(self.terrain.map[i][j]) in laser2H:
                        damage = 2
                    elif ord(self.terrain.map[i][j]) in laser3H:
                        damage = 3
                    limit.append(i)
        
        if exist :
            right_blocked = False
            limit = min(limit)
            print(limit)
            for cases in range(self.y,limit):
                print(cases)
                if self.terrain.map[cases][self.y].murD or self.terrain.map[cases][self.y].murG:
                    right_blocked = True
            if not right_blocked:
                self.life-=damage
            if right_blocked and not(self.terrains.map[self.x][self.y].murD):
                self.life-=damage              

                
    def handle_endturn(self):      
        self.check_up_laser()
        self.check_down_laser()
        self.check_left_laser()
        self.check_right_laser()
        self.MAJ()
                    
    """                   
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
        x = min(self.terrain.maxMapx, x)
        y = max(0, y)
        y = min(self.terrain.maxMapy, y)
        self.__coords = (x, y)
    """
                    
#définition des cartes à jouer
class Cartes(object):
    
    def __init__(self):
        self.priorite = 0
        self.rotation = 0
        self.nbCase = 0
        self.joueur = 0
        self.name = ''
        
    def __str__(self):
        print(self.name)
        
 
 
class CarteAvancer(Cartes):
    
    def __init__(self, nbCase):
        super(CarteAvancer, self).__init__()
        self.name = 'avancer de {}'.format(nbCase)
        self.nbCase = nbCase
        self.priorite = 100 + 200*nbCase
        
class CarteReculer(Cartes):
    
    def __init__(self):
        super(CarteReculer, self).__init__()
        self.name = 'reculer de 1'
        self.priorite = 250
        self.nbCase = -1
    
class CarteTourner(Cartes):
    
    def __init__(self, sens):
        super(CarteTourner, self).__init__()
        if sens == 1:
            self.name = 'tourner à droite'
        else:
            self.name = 'tourner à gauche'
        self.priorite = 230
        self.rotation = sens
        
    
class CarteDemiTour(Cartes):
    
    def __init__(self):
        super(CarteDemiTour, self).__init__()
        self.name = 'faire demi-tour'
        self.priorite = 200
        self.rotation = 2      
        
class Joueur():
    def __init__(self,robot,playername):
        """ Constructeur de la classe Joueur
        
        Parametres
        ----------
        robot : objet Robot
            robot du joueur
        playername : type str
            Nom du joueur
        """
        self.robot = robot
        self.name = playername
        self.robot_life = self.robot.life
        self.deck = [CarteAvancer(1)]*16+[CarteAvancer(2)]*12+[CarteAvancer(3)]*6+[CarteReculer()]*6+[CarteTourner(1)]*18+[CarteTourner(-1)]*18+[CarteDemiTour()]*6 # paquet de cartes de notre joueur
        self.choice = ['Do_nothing'] # main du joueur. Le 'Do_nothing' est présent si l'utilisateur souhaite ne pas jouer l'intégralité de ses cartes
        self.menu = [] # liste qui va être complétée par les cartes que l'utilisateur veut jouer pendant un tour 
        self.flag_nb = 0
        self.map = self.robot.terrain.map
    
    def pick_cards(self):
        """ Méthode qui régit la pioche aléatoire de cartes dans le deck
            On commence par savoir si l'utilisateur à le droit de piocher.
            Si oui, alors on choisit une carte aléatoire de son deck, que l'on ajoute à sa main (variable de type liste self.choice).
            On répète l'opération jusqu'à avoir autant de cartes que de points de vie.
            
            See also
            --------
            check_pioche() de la classe Joueur
        """
        if self.check_pioche()==True:
            self.choice = ['Do_nothing']
            deck = self.deck
            for i in range(self.robot.life):
                newcard = random.choice(deck)
                self.choice.append(newcard.name)
        else:
            print('trigger')
            self.choice = self.menu
            
    def check_pioche(self):
        """ Méthode qui vérifie, en fonction de la vie de son robot, si le joueur est autorisé à tirer des cartes de son deck
        
        Returns
        -------
        True or False : Vrai si l'utilisateur est autorisé à piocher, faux sinon
        """
        if self.robot.life < 5:
            return False # si le robot a moins de 5 PV, l'utilisateur ne pioche pas de nouvelles cartes
        else:
            return True
 
    def menu_execute(self,param):
        """ Execution d'une instruction par le robot
        
        Parametres
        ----------
        param : type str
            action à effectuer par le robot
        
        Autres variables
        ----------------
        robot.win : type booléen
            on utilise cette variable au cas où le robot atteigne le drapeau avant la fin du programme
            
        Returns
        -------
        Cette méthode ne renvoit rien, elle déclenche simplement les actions adéquates
        """
        if param== 'avancer de 1'  and not(self.robot.win):
            print('avancer de 1')
            self.robot.Forward(1, self.robot.coords, self.map)
            time.sleep(0.5)
        elif param== 'avancer de 2' and not(self.robot.win):
            print('avancer de 2')
            self.robot.Forward(2, self.robot.coords, self.map)
            time.sleep(0.5)
        elif param== 'avancer de 3' and not(self.robot.win):
            print('avancer de 3')
            self.robot.Forward(3, self.robot.coords, self.map)
            time.sleep(0.5)
        elif param=='reculer de 1'and not(self.robot.win):
            print('reculer de 1')
            self.robot.Backward(self.robot.coords, self.map)
            time.sleep(0.5)
        elif param=='tourner à droite'and not(self.robot.win):
            print('tourner à droite')
            self.robot.Turn(1)
            time.sleep(0.5)
        elif param=='tourner à gauche'and not(self.robot.win):
            print('tourner à gauche')
            self.robot.Turn(-1)
            time.sleep(0.5)
        elif param=='faire demi-tour'and not(self.robot.win):
            print('faire demi-tour')
            self.robot.Turn(2)
            time.sleep(0.5)
        else:
            pass
        self.robot.handle_land()
        self.robot.handle_endturn()

        
        
class Joueur_Humain(Joueur):
    """ Classe définissant le joueur contrôlé par un utilisateur 
        Hérite de Joueur
    """
    def __init__(self,robot,playername):
        """ Constructeur de la classe : identique à celui de la classe mère """
        super().__init__(robot,playername)
        
    def make_program(self):
        """ Réalisation d'un tour par le joueur humain
            Il est demandé au joueur de chosir un programme parmi les cartes (aléatoires) qu'il a en main
            
            Returns
            -------
            self.menu : type liste
                cartes jouées par l'utilisateur pour ce tour
        """
        pgsize=min(5,self.robot_life) # Taille du programme (il dépend de la vie du robot)
        remaining_choice = self.choice
        self.menu = []
        choix = 0
        for i in range(pgsize):
            while choix not in remaining_choice :
                print('Possibilités restantes :' )
                print(remaining_choice)
                print('Votre menu actuel')
                print(self.menu)
                choix = input("Phase N°{}?".format(i+1))
            self.menu.append(choix)
            if choix !='Do_nothing':
                remaining_choice.remove(choix)
            choix = 0
        print('Programme terminé:')
        print('Menu final',self.menu)
        return self.menu

#    
#class Joueur_Brownien(Joueur):
#    def __init__(self,robot,playername):
#        super().__init__(robot,playername)
#        
#    def make_program(self):
#        pgsize=min(5,self.robot_life)
#        remaining_choice = self.choice
#        self.menu = []
#        for i in range(pgsize):
#            new_move = random.choice(remaining_choice)
#            self.menu.append(new_move)
#            if new_move !='Do_nothing':
#                remaining_choice.remove(new_move)
#        print('Les Dés sont jettés :')
#        print('Menu : ',self.menu)
#        return self.menu

#        
#class IA_Tout_Droit(Joueur):
#    
#    def __init__(self,robot,playername):
#        super().__init__(robot,playername)
#        self.robotDir = self.robot.dir
#        self.coorFlag = self.robot.terrain.flag
#        
#    def mise_en_position(self):
#        """Définit l'orientation dans laquelle le robot doit se mettre
#        
#        Returns
#        -------
#        direction_a_prendre : type int
#            direction dans laquelle le robot doit se mettre pour aller au drapeau
#        """
#        posDrapeau = self.coorFlag
#        if self.robot.x > posDrapeau[0]:
#            direction_a_prendre = 3
#        elif self.robot.x < posDrapeau[0]:
#            direction_a_prendre = 1
#        elif self.robot.y > posDrapeau[1]:
#            direction_a_prendre = 0
#        elif self.robot.y < posDrapeau[1]:
#            direction_a_prendre = 2
#        
#        return direction_a_prendre
#
#
#    def direction_rotation(self,robotDir,orientationOpti):
#        """définit la carte à jouer pour que le robot se trouve dans la position optimale
#        
#        Parametres
#        ----------
#        robotDir : type int
#            orientation actuelle du robot
#        orientationOpti : type int
#            orientation dans laquelle le robot doit se mettre
#        
#        Returns
#        -------
#        carte_a_jouer : type str
#            mouvement à effectuer
#        """
#        carte_a_jouer = 0
#        
#        if robotDir == 0:
#            if orientationOpti == 1 :
#                carte_a_jouer = 'tourner à droite'
#            elif orientationOpti == 2:
#                carte_a_jouer == 'faire demi-tour'
#            elif orientationOpti == 3:
#                carte_a_jouer == 'tourner à gauche'
#        
#        elif robotDir == 1:
#            if orientationOpti == 2 :
#                carte_a_jouer = 'tourner à droite'
#            elif orientationOpti == 3:
#                carte_a_jouer == 'faire demi-tour'
#            elif orientationOpti == 0:
#                carte_a_jouer == 'tourner à gauche'
#                
#        elif robotDir == 2:
#            if orientationOpti == 3 :
#                carte_a_jouer = 'tourner à droite'
#            elif orientationOpti == 0:
#                carte_a_jouer == 'faire demi-tour'
#            elif orientationOpti == 1:
#                carte_a_jouer == 'tourner à gauche'
#        
#        elif robotDir == 3:
#            if orientationOpti == 0 :
#                carte_a_jouer = 'tourner à droite'
#            elif orientationOpti == 1:
#                carte_a_jouer == 'faire demi-tour'
#            elif orientationOpti == 2:
#                carte_a_jouer == 'tourner à gauche'
#                
#        return carte_a_jouer
#            
#            
#    def make_program(self):
#        pgsize = min(5,self.robot_life)
#        remaining_choice = self.choice
#        self.menu = []
#        orientationOpti = self.mise_en_position()
#        print("l'orientation optimale est : ", orientationOpti)
#        flagOrientation = False
#        flagAvancement = False
#        for i in range(pgsize):
#            rotationOpti = self.direction_rotation(self.robotDir,orientationOpti)
#            print ("la rotation optimale est : ", rotationOpti)
#            
#            if rotationOpti !=0 :
#                for carte in remaining_choice:
#                    if carte == rotationOpti:
#                        self.menu.append(carte)
#                        remaining_choice.remove(carte)
#                        flagOrientation = True
#                        break
#                    
#            if flagOrientation == False and rotationOpti != 0:
#                new_move = random.choice(remaining_choice)
#                self.menu.append(new_move)
#                if new_move !='Do_nothing':
#                    remaining_choice.remove(new_move)
#            else:
#                for cartebis in remaining_choice:
#                    if cartebis[0]=='M':
#                        self.menu.append(cartebis)
#                        remaining_choice.remove(cartebis)
#                        flagAvancement = True
#                if flagAvancement == False :
#                    new_move = random.choice(remaining_choice)
#                    self.menu.append(new_move)
#                    if new_move !='Do_nothing':
#                        remaining_choice.remove(new_move)
#                    
#        print('Les Dés sont jettés :')
#        print('Menu : ',self.menu)
#        return self.menu        
#


class Game:
    def __init__(self,terrain):
        """ Constructeur de la classe
        
        Parametres
        ----------
        terrain : fichier texte
            terrain de jeu pour la partie
        """
        self.terrain = terrain
        self.type = [Joueur_Humain] #types d'IA et humain disponibles
        self.haste = {'avancer de 3':700,'avancer de 2':500,'avancer de 1':300,'reculer de 1':200,'tourner à droite':150,'tourner à gauche':150,'faire demi-tour':150,'Do_nothing':150}
        self.robot_lst = []
        self.player_lst = []
        self.won_game = False
        self.set_parameters()
        self.Game_start()
        self.Game_master()
        
               
        
    def set_parameters(self):
        print("------------------------------------------------------")
        print("| Début du programme d'initialisation de la partie : |")
        print("------------------------------------------------------")
        player_nb = int(input("Combien de joueurs disputerons cette partie ?\n Maximum de 4 joueurs   "))
        self.player_nb = min(player_nb,4)
        print("-----------------------")
        print("| Création des Robots |")
        print("-----------------------")
        for i in range(self.player_nb):
            self.robot_lst.append(Robot(self.terrain,"Twonky"))

        for s,i in enumerate(self.robot_lst):
            i.x,i.y = self.terrain.spawn[s][0],self.terrain.spawn[s][1]
            #self.robot_lst[i].rspawn = self.terrain.spawn[i]
            
        for i in range(self.player_nb):
            type,name = 'no','no'
            print("----------------------------")
            print("|Paramétrage du joueur {} : |".format(i+1))
            print("----------------------------")
            while type not in [1,2,3]:
                type = int(input("Type du Joueur {} \n 1: Human \n 2: COM (Brownien) \n 3: COM (IA_Tout_Droit) \n".format(i+1)))
            name = input("Quel est le nom du Joueur {} ?\n".format(i+1))
            self.player_lst.append(self.type[type-1](self.robot_lst[i],name))
            
        
        return self.robot_lst,self.player_lst
    
    def make_turn(self):
        self.all_menus = []
        self.all_turn = []
        self.instructions = []
        for i in self.player_lst:
            self.all_menus.append(i.menu)
        nb_ply = len(self.all_menus)
        print('nombre de joueurs',nb_ply)
        for i in range(5):
            self.all_turn.append([])
        for i in range(5):
            for j in range(nb_ply):
                self.all_turn[i].append((self.all_menus[j][i],self.haste[self.all_menus[j][i]],j))
        for i in self.all_turn:
            i.sort(key=operator.itemgetter(1))
        for i in self.all_turn:
            self.instructions+=i
            
            
    def is_possible(self,order):
        mov = order[0]
        rob = self.robot_lst[order[2]]
        cpt = 0
        if mov not in ['avancer de 1','reculer de 1']:
            return True,[]
        elif mov =='avancer de 1':
            if rob.dir == 0:
                if self.terrain.map[rob.x-1][rob.y] !='R':
                    return True,[(0,0)]
                else:
                    for i in range(1,4):
                        if rob.x-i >=0 and self.terrain.map[rob.x-i][rob.y] =='R':
                            cpt +=1
                    if self.terrain.map[rob.x-cpt-1][rob.y] in self.terrain.non_collidable:
                        corr = [(-1,0)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x-i,rob.y))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                    
                   
                    
            elif rob.dir == 1:

                if self.terrain.map[rob.x][rob.y+1] !='R':
                    return True,[(0,0)]
                else:
                    for i in range(1,3):
                        if rob.y+i <= len(self.terrain.map[0])-1 and self.terrain.map[rob.x][rob.y+i] =='R':
                            cpt +=1
                            
                    if self.terrain.map[rob.x][rob.y+cpt+1] in self.terrain.non_collidable:
                        corr = [(0,1)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x,rob.y+i))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                    
            elif rob.dir == 2:

                if self.terrain.map[rob.x+1][rob.y] !='R':

                    return True,[(0,0)]
                else:

                    for i in range(1,3):

                        if rob.x+i <= len(self.terrain.map)-1 and self.terrain.map[rob.x+i][rob.y] =='R':
                            cpt +=1
                            

                    if self.terrain.map[rob.x+cpt+1][rob.y] in self.terrain.non_collidable:
                        corr = [(1,0)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x+i,rob.y))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                    
            elif rob.dir ==3:
                if self.terrain.map[rob.x][rob.y-1] !='R':

                    return True,[(0,0)]
                else:

                    for i in range(1,3):
                        if rob.y-i <= len(self.terrain.map[0])-1 and self.terrain.map[rob.x][rob.y-i] =='R':
                            cpt +=1
                            

                    if self.terrain.map[rob.x][rob.y-cpt-1] in self.terrain.non_collidable:
                        corr = [(0,-1)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x,rob.y-i))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
            else :
                return True,[(0,0)]
            
            
        elif mov =='reculer de 1':
            if rob.dir == 0:
                if self.terrain.map[rob.x+1][rob.y] !='R':

                    return True,[(0,0)]
                else:

                    for i in range(1,3):

                        if rob.x+i <= len(self.terrain.map)-1 and self.terrain.map[rob.x+i][rob.y] =='R':
                            cpt +=1
                            

                    if self.terrain.map[rob.x+cpt+1][rob.y] in self.terrain.non_collidable:
                        corr = [(1,0)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x+i,rob.y))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                    
            elif rob.dir == 1:
                if self.terrain.map[rob.x][rob.y-1] !='R':

                    return True,[(0,0)]
                else:

                    for i in range(1,3):
                        if rob.y-i <= len(self.terrain.map[0])-1 and self.terrain.map[rob.x][rob.y-i] =='R':
                            cpt +=1
                            

                    if self.terrain.map[rob.x][rob.y-cpt-1] in self.terrain.non_collidable:
                        corr = [(0,-1)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x,rob.y-i))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                
            elif rob.dir == 2:
                if self.terrain.map[rob.x-1][rob.y] !='R':
                    return True,[(0,0)]
                else:
                    for i in range(1,4):
                        if rob.x-i >=0 and self.terrain.map[rob.x-i][rob.y] =='R':
                            cpt +=1
                    if self.terrain.map[rob.x-cpt-1][rob.y] in self.terrain.non_collidable:
                        corr = [(-1,0)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x-i,rob.y))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
            elif rob.dir ==3:
                if self.terrain.map[rob.x][rob.y+1] !='R':
                    return True,[(0,0)]
                else:
                    for i in range(1,3):
                        if rob.y+i <= len(self.terrain.map[0])-1 and self.terrain.map[rob.x][rob.y+i] =='R':
                            cpt +=1
                            
                    if self.terrain.map[rob.x][rob.y+cpt+1] in self.terrain.non_collidable:
                        corr = [(0,1)]
                        for i in range(1,cpt+1):
                            corr.append((rob.x,rob.y+i))
                        
                        return True,corr
                    else : 
                        return False,[(0,0)]
                
            else : #avancer de 2
                return True,[(0,0)]
        
            
        
    
    def execute_turn(self):
        s=[]

        for i in self.instructions:
            if i[0]=='avancer de 3':
                s.append(('avancer de 1',0,i[2]))
                s.append(('avancer de 1',0,i[2]))
                s.append(('avancer de 1',0,i[2]))
            elif i[0]=='avancer de 2':
                s.append(('avancer de 1',0,i[2]))
                s.append(('avancer de 1',0,i[2]))
            else:
                s.append(i)
        self.instructions = s
       
            
        for i in self.instructions:
            print('Action du robot N°{} :'.format(i[2]+1))
            Bool,corr = self.is_possible(i)
            
            print('collision possible ')
            print(Bool,corr)
            if Bool :
                for h in self.robot_lst:
                    unfinished = True
                    for s in corr[1:]:
                        if unfinished:
                            if (h.x,h.y)== s :
                                h.x+=corr[0][0]
                                h.y+=corr[0][1]                            
                                unfinished = False
                                print('Application de la collision')
                                self.Game_state()
                self.player_lst[i[2]].menu_execute(i[0])

            
                
    
    def ask_players(self):
        for i in self.player_lst:
            i.pick_cards()
            i.make_program()
        self.make_turn()
        self.execute_turn()
        
    
    def evaluate_win(self):
        self.won_game = False
        for i in self.robot_lst:
            if i.win == True:
                self.won_game = True
                
    def burry_losers(self):
        for i in self.robot_lst:
            if i.life<=0:
                self.robot_lst.remove(i)
                
    def eraser_cannon(self):
        print('\n')
        print("###########################")
        print("Début de la phase de Tir")
        print("###########################")
        print('\n')
        coord=[]
        locked_up = False
        locked_right = False
        locked_down = False
        locked_left = False
        for G in self.robot_lst:
            coord.append((G.x,G.y))
        coord_set = set(coord)
        for h,i in enumerate(self.robot_lst):
            current_coord = set([(i.x,i.y)])
            target = coord_set.difference(current_coord)
            if i.dir == 0:
                for j in list(target):
                    if i.y == j[1] and i.x > j[0]:
                        locked_up = True
            elif i.dir == 1:
                for j in list(target):
                    if i.x == j[0] and i.y < j[1]:
                        locked_right = True
                
            elif i.dir == 2:
                for j in list(target):
                    if i.y == j[1] and i.x < j[0]:
                        locked_down = True
            elif i.dir == 3:
                for j in list(target):
                    if i.x == j[0] and i.y > j[1]:
                        locked_left = True
            else :
                pass
        
            if locked_up:
                for s,l in enumerate(self.robot_lst):
                    if l != i and i.y == l.y and i.x > l.x :
                        l.life -=1
                        print("le robot {} s'est fait fumé par le robot {}".format(s+1,h+1))
            
            if locked_right:
                for s,l in enumerate(self.robot_lst):
                    if l != i and i.x == l.x and i.y < l.y :
                        l.life -=1
                        print("le robot {} s'est fait fumé par le robot {}".format(s+1,h+1))
            
            
            if locked_down:
                for s,l in enumerate(self.robot_lst):
                    if l != i and i.y == l.y and i.x < l.x :
                        l.life -=1
                        print("le robot {} s'est fait fumé par le robot {}".format(s+1,h+1))
                    

            if locked_left:
                for s,l in enumerate(self.robot_lst):
                    if l != i and i.x == l.x and i.y > l.y :
                        l.life -=1
                        print("le robot {} s'est fait fumé par le robot {}".format(s+1,h+1))
                
    def Game_start(self):
        print("##################")
        print("Debut de la partie")
        print("##################")
        self.Game_state()
        for s,i in enumerate(self.robot_lst):
            print('le robot {} est en position {}'.format(s+1,(i.x,i.y)))
        
    def Game_state(self):
        a = self.terrain.map
        for c,s in enumerate(a):
            for g,o in enumerate(s):
                if s[g]=='R':
                    s[g]==self.terrain.mapInit[c][g]
        for i in self.robot_lst:
            a[i.x][i.y]='R'
        print("voila ce qu'il y a après")
        for i in self.player_lst:
            print("###########################")
            print("{} et son robot {}".format(i.name,i.robot.name))
            print("position : ({},{})".format(i.robot.x,i.robot.y))
            print("Points de Vie actuels : {}".format(i.robot.life))
            print("Direction actuelle : {}".format(i.robot.orientation))
            print("###########################")
            print('\n')
            
        
    
    def Finished(self):
        print("############")
        print("Jeu Terminé")
        print("############")
    
    def Victory(self):
        for s,i in enumerate(self.robot_lst):
            if i.win == True:
                winner = s
        print("#####################")
        print("Annonce des résultats")
        print("#####################")
        print('VICTOIRE DU JOUEUR ',self.player_lst[winner].name)
        print('Félicitation')
        
    def Game_over(self) :
        print("#####################")
        print("Annonce des résultats")
        print("#####################")
        print("Tous les Compétiteurs ont été détruits")
        print("G-A-M-E__O-V-E-R")
                
                
        
    def Game_master(self):
        while not(self.won_game) and len(self.robot_lst)>=1:
            self.ask_players()
            self.eraser_cannon()
            self.burry_losers()
            self.evaluate_win()
            self.Game_state()
        if self.won_game:
            self.Finished()
            self.Victory()
        if len(self.robot_lst)<=0:
            self.Finished()
            self.Game_over()
