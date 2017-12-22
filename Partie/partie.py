import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders' )
import attribut.attributs as A
import carte.carte
import Joueur.Joueur as J
import Wonder.wonder

Liste_joueurs = list[]
Science = dict(A.Science)

#fonction pour compter les points de Science
def pvscience(Science) :
    Total = 0
    Total += Science['Psm'] * Science['Psm']
    Total += Science['Pse'] * Science['Pse']
    Total += Science['Psi'] * Science['Psi']
    mem = 10
    for domaine, val in Science.items() :
        if Science[domaine] < mem :
            mem = val
    Total += 7*mem
    return Total

Guerre = dict(A.Armee)

#fonction pour compter les points de baston !
def pvGuerre(Guerre)
    Total = 0
    Total += Guerre['Pv1']
    Total += Guerre['PV3'] * 3
    Total += Guerre['PV5'] * 5
    Total -= Guerre['PD']
    return Total

#fonction qui reçoit un nombre de joueurs et renvoie une liste de joueurs initialisée
def Init_Partie(nb_joueur) :
    Liste_r=list[]
    for i in nb_joueur :
        Liste_r[i]=J.Init_Joueur
    return Liste_r

#fonction qui prend en argument une liste de joueurs et qui dit qui a gagné
def Fin_de_Partie(Liste_joueurs):
    liste_point = list()
    for jo in enumerate(Liste_joueurs) :
        Or = jo[1]['attributs']['Production_s']['Or']
        PVOR = (Or - Or % 3) /3
        liste_point[jo[0]] = pvscience(jo[1]['attributs']['Science']) + PVOR + pvGuerre(jo[1]['attributs']['Armee']) + jo[1]['attributs']['nbr_PV']
    for tupple_point in enumerate(liste_point) :
        print("le joueur" tupple_point[0]+1 "a marqué" tupple_point[1] "points")
        print("c'est la fin du jeu ! GG WP")

#fonction qui prend en argument un nombre de joueur et qui retourne une liste de cartes randomisée : paquet
def Init_Paquet(nb_joueurs, age):


def Distribuer_Cartes(age, Liste_joueurs, paquet):

