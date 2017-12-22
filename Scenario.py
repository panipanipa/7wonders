import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders')
import Joueur.Joueur as J
import attribut.attributs as A
import carte.carte as C
import Wonder.wonder as W

Joueur1 = dict(J.Joueur)
Joueur2 = dict(J.Joueur)
Joueur3 = dict(J.Joueur)

merveille = W.wonder

Joueur1 = J.Init_Joueur(merveille)
Joueur2 = J.Init_Joueur(merveille)
Joueur3 = J.Init_Joueur(merveille)

#Joueur1['attributs']['Ressources_s']['Bois'] = 1

#Joueur1['attributs']= attribut.attributs.init_attribut()
#Joueur2['attributs']= attribut.attributs.init_attribut()
#Joueur3['attributs']= attribut.attributs.init_attribut()

karte = dict(C.carte)
cout_k = "Pierre 1"
karte['nom'] = "Bains"
karte['couleur'] = 'b'
karte['id'] = 3
if karte['pre'](Joueur1['attributs'], cout_k, 3, Joueur1['attributs']['liste_id'], 0):
    karte['post']("Nbr_PV 3", Joueur1['attributs'])
    Joueur1['attributs']['liste_id'].append(karte['id'])

print("joueur 1 :\n" , Joueur1)

karte = dict(C.carte)
cout_k = ""
karte['nom'] = "Chantier"
karte['couleur'] = 'm'
karte['id'] = 9
if karte['pre'] (Joueur2['attributs'] , cout_k, 9, Joueur2['attributs']['liste_id'], 0):
    karte['post']("Bois 1", Joueur2['attributs']['Production_s'])
    Joueur2['attributs']['liste_id'].append(karte['id'])

print("joueur 2 : \n" , Joueur2)

karte = dict(carte.carte.carte)
cout_k = ""
karte['nom'] = "Cavite"
karte['couleur'] = 'm'
karte['id'] = 14
if karte['pre'] (Joueur3['attributs'] , cout_k, 14, Joueur3['attributs']['liste_id'], 0):
    karte['post']("Pierre 1", Joueur3['attributs']['Production_s'])
    Joueur3['attributs']['liste_id'].append(karte['id'])

print("joueur 3 : \n" , Joueur3)

# tour 2

Joueur1['attributs']['Production_s']['Or'] += 2
Joueur.Joueur.achat(Joueur1['attributs'], Joueur2['attributs'], "Bois 1", "droite")
karte = dict(carte.carte.carte)
cout_k = "Bois 1"
karte['nom'] = "Palissade"
karte['couleur'] = 'r'
karte['id'] = 29
if karte['pre'] (Joueur1['attributs'] , cout_k, 29, Joueur1['attributs']['liste_id'], 0):
    karte['post']("Force 1", Joueur1['attributs'])
    Joueur3['attributs']['liste_id'].append(karte['id'])

print("joueur 1 : \n" , Joueur1)


karte = dict(carte.carte.carte)
cout_k = "Pierre 1"
karte['nom'] = "Bains"
karte['couleur'] = 'b'
karte['id'] = 3
if karte['pre'] (Joueur3['attributs'] , cout_k, 3, Joueur3['attributs']['liste_id'], 0):
    karte['post']("Nbr_PV 3", Joueur3['attributs'])
    Joueur3['attributs']['liste_id'].append(karte['id'])

karte = dict(carte.carte.carte)
cout_k = "Pierre 3"
karte['nom'] = "Aqueduc"
karte['couleur'] = 'b'
karte['id'] = 50
if karte['pre'] (Joueur3['attributs'] , cout_k, 50, Joueur3['attributs']['liste_id'], 3):
    karte['post']("Nbr_PV 5", Joueur3['attributs'])
    Joueur3['attributs']['liste_id'].append(karte['id'])


print("joueur 3 : \n" , Joueur3)
# print(Joueur3['attributs'] is Joueur1['attributs'])

