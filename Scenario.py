import attribut.attributs
import carte.carte

Joueur = dict()
Joueur = {'attributs': attribut.attributs.Attributs,\
          'wonder': "indetermine"}

Joueur1 = dict(Joueur)
Joueur2 = dict(Joueur)
Joueur3 = dict(Joueur)

Joueur1['attributs']= attribut.attributs.init_attribut()
Joueur2['attributs']= attribut.attributs.init_attribut()
Joueur3['attributs']= attribut.attributs.init_attribut()

karte = dict(carte.carte.carte)
cout_k = "Pierre 1"
karte['nom'] = "Bains"
karte['couleur'] = 'b'
karte['id'] = 3
if karte['pre'] (Joueur1['attributs'] , cout_k, 3, Joueur1['attributs']['liste_id'], 0):
    karte['post']("Nbr_PV 3", Joueur1['attributs'])
    Joueur1['attributs']['liste_id'].append(karte['id'])

print("joueur 1 :\n" , Joueur1)

karte = dict(carte.carte.carte)
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

