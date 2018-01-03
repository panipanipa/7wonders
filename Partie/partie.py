import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders' )
import attribut.attributs as A
import pandas
import carte.carte as C
import Joueur.Joueur as J
import Wonder.wonder

Liste_joueurs = list()
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
def pvGuerre(Guerre):
    Total = 0
    Total += Guerre['Pv1']
    Total += Guerre['PV3'] * 3
    Total += Guerre['PV5'] * 5
    Total -= Guerre['PD']
    return Total

#fonction qui reçoit un nombre de joueurs et renvoie une liste de joueurs initialisée
def Init_Partie(nb_joueur) :
    Liste_r=list()
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
        print("le joueur", tupple_point[0]+1 , "a marqué" , tupple_point[1] , "points")
        print("c'est la fin du jeu ! GG WP")



#fonction qui prend en argument un nombre de joueur et qui retourne une liste de cartes randomisée : paquet
def Init_Paquet(nb_joueurs, age):
    paquet = list[]
    df_e = pandas.read_excel("7wonder_cartes.xlsx","Sheet1")
    data_array = df_e.values
    if age == 1 :
        for i in range(0,48) :
            if data_array[i][2] <= nb_joueurs :
                carte = C.Init_Carte(i, data_array)
                # aurais-tu l'extrême bonté et l'ultime magnanimitude de bien vouloir vérifier cette ligne DENIS, s'il t'en plait
                paquet.append(carte)
    if age == 2 :
        for i in range(49,97) :
            if data_array[i][2] <= nb_joueurs :
                carte = C.Init_Carte(i, data_array)
                # aurais-tu l'extrême bonté et l'ultime magnanimitude de bien vouloir vérifier cette ligne DENIS, s'il t'en plait
                paquet.append(carte)
    if age == 3 :
        for i in range(98,137) :
            if data_array[i][2] <= nb_joueurs :
                carte = C.Init_Carte(i, data_array)
                # aurais-tu l'extrême bonté et l'ultime magnanimitude de bien vouloir vérifier cette ligne DENIS, s'il t'en plait
                paquet.append(carte)
        liste_guilde = list()
        nb_guilde_ajout = nb_joueurs + 2
        for i in range(142,153) :
            carte = C.Init_Carte(i, data_array)
            # aurais-tu l'extrême bonté et l'ultime magnanimitude de bien vouloir vérifier cette ligne DENIS, s'il t'en plait
            liste_guilde.append(carte)


    return paquet
paquet = list()

#fonction qui, a partir d'un paquet pas randomisé, distribue des mains random aux joueurs
#on a besoin de random.py
def Distribuer_Paquet(paquet, Liste_joueurs) :
    i = len.paquet
    while i != 0 :
    #tant qu'il reste des cartes à distribuer
        for Jou in Liste_joueurs :
        # Pour chacun des joueurs
            while len.Jou['cartes'] != 7 :
            #tant qu'ils ont pas 7 cartes
                a = R.randint(0,i)
                Jou['cartes'].append(paquet[a])
                del paquet[a]
                i = i-1
            #je leur donne une carte random, je l'enlève de la liste


def Distribuer_Cartes(age, Liste_joueurs, paquet):
    return
