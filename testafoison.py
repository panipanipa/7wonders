import attribut.attributs
import carte.carte

Liste_Joueurs = list()
at_Joueur = attribut.attributs


#carte.carte.test_trigger("Bois 2", attribut.attributs.Production_simple_exemple)

karte = dict(carte.carte.carte)
karte['nom'] = "Bains"
#karte.cout = ""
#karte.post = carte.carte.Trigger_effet("PV 3", at_Joueur)

at1 = dict(attribut.attributs.Attributs)
at1['Production_s']['Bois'] = 2
at1['Production_s']['Pierre'] = 3

cout = "Bois 2 Pierre 2"
info = cout.split(" ")
print(carte.carte.Ressources_presente(at1, "Bois 2 Pierre 4"))
#print(attribut.attributs.Ressources['Bois'])



#def Init_Joueurs(Liste_Joueurs):
    #Nbr_j = input("Combien de joueurs etes-vous ? ")
    #for i in range(Nbr_j-1):
        #Joueurs_'i' = Joueurs
        #Liste_Joueurs.append(Joueurs_'i')