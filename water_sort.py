# Créé par petibonm, le 03/02/2023 en Python 3.7
from graphics import *
from water_sort_graphics import *
from random import randint,choice,shuffle
from time import sleep



class Jeu:

    def __init__(self,nb_tubes,capacite_tube):
        self.hauteur=500
        self.largeur=1250
        self.nb_tube=nb_tubes
        self.capacite_tube=capacite_tube
        self.liste_couleur=[rouge,jaune,rose,orange,violet,bleu,cyan,vert_clair,bleu_clair,rouge_fonce,bleu_fonce,vert_fonce,marron,
        couleur_hasard1,couleur_hasard2,couleur_hasard3,couleur_hasard3,couleur_hasard4,couleur_hasard5,couleur_hasard6,couleur_hasard7,
        couleur_hasard8,couleur_hasard9,couleur_hasard10,couleur_hasard11,couleur_hasard12,couleur_hasard13,couleur_hasard14,couleur_hasard15]
        self.liste_tubes=self.creation_tubes()
        self.coordonnes_tubes=self.placement_tube()
        self.tube_select=-1
        # quand self.tube_select vaut -1, cela signifie qu'aucun tube n'est sélectionné
        self.liste_tubes_select=[]
        self.historique=[]
        self.derniere_partie_modif=self.liste_tubes
        self.interface=Interface(self.largeur,self.hauteur,self.capacite_tube,self.nb_tube)


    def demarre(self):
        self.interface.afficher_debut()
        self.stocker_action(self.liste_tubes)
        self.liste_tubes_select.append(self.tube_select)
        while not(self.fin()):
            self.dessiner_tubes(self.tube_select)
            affiche_auto_on()
            self.interface.afficher_melanger_et_bouton_retour()
            clic=wait_clic()
            if clic:
                x,y=clic
                if x>=10 and x<=305 and y>=10 and y<=60:
                    if type(self.historique[-1])==tuple:
                        self.stocker_action(self.liste_tubes)
                        self.f=self.liste_tubes
                    self.liste_tubes=self.creation_tubes()
                    self.stocker_action(self.liste_tubes)

                if x>=self.largeur-140 and x<=self.largeur-10 and y>=10 and y<=60:
                    if len(self.historique)==0:
                        pass
                    else:
                        if len(self.historique)==1:
                            retour=self.revenir_en_arriere()
                            self.historique.append(retour)
                        else:
                            retour=self.revenir_en_arriere()
                        if type(retour)==list:
                            if retour==self.liste_tubes:
                                if len(self.historique)==1:
                                    pass
                                else:
                                    retour2=self.revenir_en_arriere()
                                    self.liste_tubes=retour2
                            else:
                                self.liste_tubes=retour
                            self.affiche_eau_tube_retour2(self.derniere_partie_modif)
                            affiche_auto_on()
                        if type(retour)==tuple:
                            self.vider_retour(retour[0],retour[1],retour[2])
                            self.affiche_eau_tube_retour(retour[0],retour[1])
                            affiche_auto_on()
                else:
                    self.liste_tubes_select.append(self.tube_select)
                    self.dessiner_tube_selectionne(clic)
                    vider=self.vider_dans(self.liste_tubes[self.liste_tubes_select[-1]],self.liste_tubes[self.tube_select])
                    if vider==None or self.clic_dehors(clic)==0:
                        pass
                    else:
                        self.stocker_action(vider)
        sleep(0.5)
        self.interface.afficher_fin()
        attendre_echap()


    def creation_tubes(self):
        tubes_couleurs=[]
        couleurs_non_utilisés=[]
        random.shuffle(self.liste_couleur)
        for i in range(self.nb_tube):
            tubes_couleurs.append([])
            if i < self.nb_tube - 2:
                for j in range(self.capacite_tube):
                    couleurs_non_utilisés.append(self.liste_couleur[i])
        for i in range(self.nb_tube - 2):
            for j in range(self.capacite_tube):
                couleur = random.choice(couleurs_non_utilisés)
                tubes_couleurs[i].append(couleur)
                couleurs_non_utilisés.remove(couleur)
        return tubes_couleurs


    def placement_tube(self):
        dictio_coordonnee={}
        espace_largeur=self.largeur/self.nb_tube
        for i in range(self.nb_tube):
            dictio_coordonnee[i]=coordonnee_tube=((30+espace_largeur*i,50),((30+(self.largeur*2/3)/self.nb_tube)+espace_largeur*i,self.hauteur-50))
        return dictio_coordonnee


    def dessiner_tubes(self,nb_tube_select):
        affiche_auto_off()
        for i,valeur in enumerate(self.liste_tubes):
            if len(valeur)==0:
                for k in range(self.capacite_tube):
                    self.interface.afficher_eau(i,k,noir)
            if i==self.liste_tubes_select[-1]:
                    if len(valeur)<self.capacite_tube:
                        for k in range(len(valeur),self.capacite_tube):
                            self.interface.afficher_eau(i,k,noir)
            for j in range(len(valeur)):
                self.interface.afficher_eau(i,j,self.chercher_couleur(i,j))
            if i==self.tube_select:
                self.interface.afficher_tube(i,blanc)
            else:
                self.interface.afficher_tube(i,gris_fonce)


    def dessiner_tube_selectionne(self,clic):
        x,y=clic
        for cle,valeur in self.coordonnes_tubes.items():
            if x>=valeur[0][0] and x<=valeur[1][0] and y>=valeur[0][1] and y<=valeur[1][1]:
                if self.tube_select==cle:
                    self.tube_select=-1
                else:
                    self.tube_select=cle


    def vider_dans(self,source,destination):
        if len(destination)==self.capacite_tube:
            return None
        if self.tube_select>=0 and self.liste_tubes_select[-1]>=0 :
            if len(source)==1:
                vider=self.vider_une_couleur(source,destination)
                return vider
            if len(source)>=2:
                if len(self.nb_couleurs_identiques(source))>=2:
                    couleur_a_deplace=self.nb_couleurs_identiques(source)
                    plusieurs_couleur=[]
                    for same_color in reversed(source):
                        if same_color==couleur_a_deplace[0]:
                            if len(destination)==self.capacite_tube:
                                return (self.indice_tube(source),self.indice_tube(destination),plusieurs_couleur)
                            else:
                                if len(couleur_a_deplace)==1:
                                    vider=self.vider_une_couleur(source,destination)
                                    if vider==None:
                                        return None
                                    else:
                                        plusieurs_couleur.append(vider[2][0])
                                    return (vider[0],vider[1],plusieurs_couleur)
                                else:
                                    vider=self.vider_une_couleur(source,destination)
                                    couleur_a_deplace.pop()
                                    if vider==None:
                                        return None
                                    else:
                                        plusieurs_couleur.append(vider[2][0])
                        if same_color!=couleur_a_deplace[0]:
                            return (self.indice_tube(source),self.indice_tube(destination),couleur_a_deplace)
                else:
                    vider=self.vider_une_couleur(source,destination)
                    return vider


    def vider_une_couleur(self,source,destination):
        if len(destination)==0 or source[-1]==destination[-1]:
            couleur_a_deplace=source.pop()
            destination.append(couleur_a_deplace)
            return (self.indice_tube(source),self.indice_tube(destination),[couleur_a_deplace])
        else:
            return None


    def vider_retour(self,indice_destination,indice_source,couleurs):
        for valeur in couleurs[:]:
            if not(self.liste_tubes[indice_source]) or len(self.liste_tubes[indice_destination])==self.capacite_tube:
                return
            else:
                couleur_a_deplace=self.liste_tubes[indice_source].pop()
                self.liste_tubes[indice_destination].append(couleur_a_deplace)


    def fin(self):
        gagne=False
        nb_tube_fini=0
        for valeur in self.liste_tubes:
            if all(couleur==valeur[0] for couleur in valeur) or len(valeur)==0:
                if len(valeur)==self.capacite_tube or len(valeur)==0:
                    nb_tube_fini+=1
        if nb_tube_fini==self.nb_tube:
            gagne=True
        else:
            gagne=False
        return gagne


    def stocker_action(self,element):
        self.historique.append(element)


    def revenir_en_arriere(self):
        retour=self.historique.pop()
        return retour


    def affiche_eau_tube_retour(self,indice_tube1,indice_tube2):
        # fonction annexe qui règle des bugs d'affichage sur le retour en arriere
        affiche_auto_off()
        if len(self.liste_tubes[indice_tube1])<self.capacite_tube:
            for k in range(len(self.liste_tubes[indice_tube1]),self.capacite_tube):
                self.interface.afficher_eau(indice_tube1,k,noir)
        if len(self.liste_tubes[indice_tube2])<self.capacite_tube:
            for k in range(len(self.liste_tubes[indice_tube2]),self.capacite_tube):
                self.interface.afficher_eau(indice_tube2,k,noir)


    def affiche_eau_tube_retour2(self,liste_tube):
        # fonction annexe qui règle des bugs d'affichage sur le retour en arriere
        affiche_auto_off()
        for i,tube in enumerate(liste_tube):
            for k in range(len(tube),self.capacite_tube):
                self.interface.afficher_eau(i,k,noir)


    def chercher_couleur(self,indice_tube,num_couleur):
        tube=self.liste_tubes[indice_tube]
        return tube[num_couleur]


    def clic_dehors(self,clic):
        x,y=clic
        nb=0
        for valeur in self.coordonnes_tubes.values():
            if x>=valeur[0][0] and x<=valeur[1][0] and y>=valeur[0][1] and y<=valeur[1][1]:
                nb=1
        return nb


    def indice_tube(self,tube):
        for i,val in enumerate(self.liste_tubes):
            if val==tube:
                return i


    def nb_couleurs_identiques(self,liste):
        liste_couleurs_identiques=[]
        couleur=liste[-1]
        for valeur in reversed(liste):
            if valeur==couleur:
                liste_couleurs_identiques.append(valeur)
        return liste_couleurs_identiques

nb_tubes=int(input("Combien de tubes voulez-vous dans la partie ? (valeur optimale : 8)"))
capacite_tube=int(input("Combien d'étages d'eau par tube voulez-vous dans la partie ? (valeur optimale : 4)"))
jeu=Jeu(nb_tubes,capacite_tube)
jeu.demarre()





