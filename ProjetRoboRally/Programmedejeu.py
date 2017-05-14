# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:26:38 2017

@author: Romain
"""
import random as rd
import plateau as pl
import DefinitionClasse as cl

"""""""""""""""
Fonctions
"""""""""""""""


def DistributionCartes(listeJoueur):
    nbJoueur = len(listeJoueur)
    Choix = [cl.CarteAvancer, cl.CarteReculer, cl.CarteTourner, cl.CarteDemiTour]
    
    for i in range(nbJoueur):
        listeJoueur[i].cartes = []
        for j in range(min(listeJoueur[i].vie, 5)):
            alea = rd.randint(0, 3)
            listeJoueur[i].cartes.append(Choix[alea]) #on ajoute une carte aléatoire dans la main du joueur
            


def Initialisation(nbJoueur, nbIA):
    #définition des joueurs     
    global Joueur
    Joueur = []
    global Bot
    Bot = []
    #définition du plateau
    plateau = pl.Map('fichier.txt', 'r')
    #ajout des utilisateurs
    for i in range(nbJoueur):
        Joueur.append(cl.Utilisateur(plateau))
    for  j in range(nbIA):
        Bot.append(cl.IA(plateau))
    
    DistributionCartes(nbjoueur)
    


    



def Jeu():
    nbJoueur = input("entrer le nombre de joueur: ")
    Initialisation(nbJoueur, 0)    
    
    while finish == 0:
        unTour(nbJoueur, 0)
    




