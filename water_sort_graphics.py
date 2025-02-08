# Créé par petibonm, le 03/02/2023 en Python 3.7

from graphics import *
from random import randint

gris_fonce=obtenir_couleur(128,128,128)
couleur_hasard1=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard2=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard3=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard4=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard5=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard6=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard7=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard8=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard9=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard10=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard11=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard12=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard13=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard14=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))
couleur_hasard15=obtenir_couleur(randint(0,255),randint(0,255),randint(0,255))



class Interface:

    def __init__(self,largeur,hauteur,capacite_tube,nb_tube):
        self.largeur,self.hauteur=largeur,hauteur
        self.capacite_tube=capacite_tube
        self.nb_tube=nb_tube


    def afficher_debut(self):
        init_fenetre(self.largeur,self.hauteur,"Water Sort")
        modifie_taille_image("fond.jpg",self.largeur,self.hauteur)
        affiche_image("fond.jpg",(0,0))


    def afficher_eau(self,numero_tube,etage_couleur,couleur):
        espace_largeur=self.largeur/self.nb_tube
        espace_hauteur=(self.hauteur-100)/self.capacite_tube
        affiche_rectangle_plein((30+espace_largeur*numero_tube,75+espace_hauteur*etage_couleur),((30+(self.largeur*2/3)/self.nb_tube)+espace_largeur*numero_tube,
        ((self.hauteur-100)/self.capacite_tube)+75+espace_hauteur*etage_couleur),couleur)


    def afficher_tube(self,numero_tube,couleur,epaisseur=1):
        espace_largeur=self.largeur/self.nb_tube
        affiche_rectangle((30+espace_largeur*numero_tube,75),((30+(self.largeur*2/3)/self.nb_tube)+espace_largeur*numero_tube,self.hauteur-25),couleur,7)


    def afficher_melanger_et_bouton_retour(self):
        affiche_rectangle_plein((10,10),(305,60),blanc)
        affiche_texte("Nouvelle partie",(15,13),bleu_fonce,40,"Arial")
        affiche_image("retour_arriere.jpg",(self.largeur-140,10))


    def afficher_fin(self):
        remplir_fenetre(noir)
        modifie_taille_image("fond_fin.jpg",self.largeur,self.hauteur)
        affiche_image("fond_fin.jpg",(0,0))





