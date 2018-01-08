import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders' )
import attribut.attributs as A
import pandas
import carte.carte as C
import Joueur.Joueur as J
import random.py as R
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
    paquet = list()
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
        while nb_guilde_ajout != 0:
            a = R.randint(0, len.liste_guilde)
            paquet.append(liste_guilde[a])
            del liste_guilde[a]
            nb_guilde_ajout = nb_guilde_ajout - 1
        return paquet


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


def Jouer_Carte(Joueur, Defausse) :
    Jouee = False
    while Jouee == False :
        A = input("Sélectionnez une carte en indiquant sa position dans votre main (start à 1)")
        #On demande au joueur d'indiquer la carte avec laquelle il va intéragir
        Boo = input("Que voulez vous en faire ? 1 == la jouer     2 == la défausser")
        #Il indique comment il va intéragir avec, il faudra implémenter le fait de construire la merveille
        if Boo == 2 :
            Defausse.append(Joueur['cartes'][A])
            del Joueur['cartes'][A]
            Joueur['Attributs']['Ressources_S']['Or'] += 3
            Jouee = True
        if Boo == 1 :
            if Joueur['cartes'][A]['pre'](Joueur['Attributs']) :
                Joueur['cartes'][A]['post'](Joueur['Attributs'])
                del Joueur['cartes'][A]
                Jouee = True
            else :
                print("vous ne pouvez pas jouer cette carte")
        else :
            print("vous avez entré une valeur invalide")

             
def Swap_main(age, Liste_Joueurs) :
    if age == 1 or age == 3 :
    #on regarde si on change à droite ou a gauche
        aux = Liste_Joueurs[-1]['cartes']
        for Jou in len.Liste_Joueurs :
            if Jou != len.Liste_Joueurs :
                Liste_Joueurs[-Jou]['cartes'] = Liste_Joueurs[-Jou-1]['cartes']
            else :
                Liste_Joueurs[-Jou]['cartes'] = aux
    if age == 2 :
        aux = Litse_Joueurs[0]
        for Jou in len.Liste_Joueurs :
            if Jou != len.Liste_Joueurs :
                Liste_Joueurs[Jou]['cartes'] = Liste_Joueurs[Jou+1]['cartes']
            else :
                Liste_Joueurs[Jou]['cartes'] = aux

cel_achat = dict()
cel_achat = {'id_joueur' : 0, \
'montant' : 0, \
'Ressources' : dict(A.Ressources), \
'orientation' : 0}

def Phase_Achat(Liste_Joueurs) :
    liste_trig_achat = list()
    #On va faire nos achats dans un premier temps, les rendre effectifs dans un second temps, la on crée des mémoires
    for num, Jou in enumerate.Liste_Joueurs :
    #On énumère nos joueurs
        print("c'est au joueur ")
        print(num+1)
    #Ne pas oublier de montrer les cartes
        A = input("voulez vous acheter des ressources ? 1 pour oui 0 pour non")
        while A :
    #La phase d'achat
            O = input ("D pour acheter à droite, G pour acheter à gauche")
            Ress_Achat = dict(A.Ressources)
            for Re in Ress_Achat.keys :
                I = input("combien voulez vous acheter de " + Re)
                Ress_Achat[Re] = I
    #A ce moment, on a constitué notre répertoire de ressources à acheter
            if O == 'D' :
                orientation = 'droite'
                o = 1
            if O == 'G' :
                orientation = 'gauche'
                o = -1
            Vendeur = Liste_Joueurs[num+o % len.Liste_Joueurs]
    #Ici on différencie les cas droite et gauche
            if J.ressource_achetable(Vendeur['Attribut'], Ress_Achat) :
                m = J.montant_a_payer(Jou['Attributs'],Ress_Achat,orientation)
                if m <=Jou['Attributs']['Ressources_Simples']['Or'] :
                    Achat = dict(cel_achat)
                    Achat['id_joueur'] = num
                    Achat['montant'] = m
                    Achat['Ressources'] = Ress_Achat
                    Achat['orientation'] = o
                    liste_trig_achat.append(Achat)
    #On stocke en mémoire les infos nécesaires pour trigger les achats
                else :
                    print("vous n'avez pas d'or pour faire ça ...")
            else :
                print("le joueur n'a pas ces ressources")
            A = input("voulez-vous acheter autre chose ? 1 pour oui 0 pour non")
    for c_achat in liste_trig_achat :
        J.trigger_achat_ressources(Liste_Joueurs[c_achat['id_joueur']]['Attributs'],Liste_Joueurs[c_achat['id_joueur']+c_achat['orientation']%len.Liste_Joueurs]['Attributs'],c_achat['montant'],c_achat['Ressources'])
    #maintenant qu'on s'est assurer que tout le monde peut ou non faire ses actions, on les fait
    #ça évite les problèmes de simultanéité
                            
def Phase_Jeu(Liste_Joueurs, Defausse) :            
    print("Sélectionnez votre carte et ce que vous voulez en faire")
    for Jou in Liste_Joueurs :
        Jouer_Carte(Jou, Defausse)

def Age(ag, Liste_Joueurs, Defausse) :
    paq = Init_Paquet(len.Liste_Joueurs,ag)
    Distribuer_Paquet(paq, Liste_Joueurs)
#init du paquet et distribution des cartes
    for a in (1,6) :
        print("phase"+str(a)+"de l'age"+str(ag))
        Phase_Achat(Liste_Joueurs)
        Phase_Jeu(Liste_Joueurs,Defausse)
        Swap_main(ag, Liste_Joueurs)
#Les tours de jeu
    for num, Jou in enumerate.Liste_Joueurs :
#rajouter un cas pour la merveille ui fait qu'on peut jouer nos 2 dernières cartes ici, pas obligatoire maintenant
        Defausse.append(Jou['cartes'][0])
        del Jou['cartes'][0]
        if ag == 1 :
            if Jou['Attributs']['Force'] > Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV1'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1
            if Jou['Attributs']['Force'] > Liste_Joueurs[num-1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV1'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1
        if ag == 2 :
            if Jou['Attributs']['Force'] > Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV3'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1
            if Jou['Attributs']['Force'] > Liste_Joueurs[num-1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV3'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1
        else :
            if Jou['Attributs']['Force'] > Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV5'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1
            if Jou['Attributs']['Force'] > Liste_Joueurs[num-1 % len.Liste_Joueurs]['Attributs']['Force'] :
                Jou['Attributs']['Armee']['PV5'] += 1
                Liste_Joueurs[num+1 % len.Liste_Joueurs]['Attributs']['Armee']['PD'] += 1

def Partie() :
    j=input("combien de joueurs etes vous ?")
    Liste_J=Init_Partie(j)
    Defausse=list()
    Defausse=[]
    Age(1,Liste_j,Defausse)
    Age(2,Liste_j,Defausse)
    Age(3,Liste_j,Defausse)
    Fin_de_Partie(Liste_J)