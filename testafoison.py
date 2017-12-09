import attribut.attributs
import carte.carte

Liste_Joueurs = list()
at_Joueur = attribut.attributs.init_attribut()


#at1 = dict(attribut.attributs.Attributs)
#at1['Production_s'] = dict(attribut.attributs.Attributs['Production_s'])
at1 = attribut.attributs.init_attribut()
at1['Production_s']['Bois'] = 2
at1['Production_s']['Pierre'] = 3
#print(at1['Production_s'] is attribut.attributs.Attributs['Production_s'])


# carte.carte.test_trigger("Bois 2", attribut.attributs.Production_simple_exemple)

# fonction de test propre de ressources presentes
# cout et att sont des strings separes par le caractere ' '

def test_ressources_presente (cout, att):
    at = attribut.attributs.init_attribut()
    att_inf = att.split(' ')
    i = 0
    while i<len(att_inf):
        at['Production_s'][att_inf[i]] = int(att_inf[i+1])
        i += 2

    info = cout.split(" ")
    return carte.carte.Ressources_presente(at, cout)

    #print(carte.carte.Ressources_presente(at1, cout))

# fonction de test de deja_jouee
# att est un attribut // liste_int est une liste contenant des entiers // id_test est l'entier que l'on teste
def test_deja_jouee (liste_int, att, id_test):
    card=len(liste_int)
    for i in range(card):
        att['liste_id'].append(liste_int[i])
    return carte.carte.Est_deja_jouee(id_test, att)

# fonction de test de est chainable id
# att est un attribut // liste_int est une liste contenant des entiers // id_carte est l'entier que l'on teste
def test_est_chainable_id(id_carte, liste_int, att):
    card = len(liste_int)
    for i in range(card):
        att['liste_id'].append(liste_int[i])
    return carte.carte.Est_chainable_id(id_carte, liste_int)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# endroit ou on fait tous les test (c'est un peu le bordel)

cout = "Bois 2 Pierre 2"
att_s = "Bois 2 Pierre 3"
print("test de ressources presentes // atendu : true // recu :", test_ressources_presente(cout, att_s), "\n")

liste_int = [1, 2, 3, 4]
att = attribut.attributs.init_attribut()
print("test de deja jouee // attendu : true // recu :", test_deja_jouee(liste_int, att, 4), "\n")
print("test de deja jouee // attendu : false // recu :", test_deja_jouee(liste_int, att, 5), "\n")

print("test de est chainable // attendu : true // recu :", test_est_chainable_id(3, liste_int, att), "\n")
print("test de est chainable // attendu : false // recu :", test_est_chainable_id(5, liste_int, att), "\n")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# creation a la main de la carte bain (cf google drive)
att_k = dict()
att_k = attribut.attributs.init_attribut()

cout_k = "Pierre 1"
karte = dict(carte.carte.carte)
karte['nom'] = "Bains"
karte['couleur'] = 'b'
karte['id'] = 3
# karte['post'] = carte.carte.Trigger_effet
# karte['pre'] (att_k, cout_k, 0, att_k['liste_id'], 0)

print("test de la karte : \n")
print("nom // attendu : bains // recu :", karte['nom'], "\n")
print("couleur // attendu : b // recu :", karte['couleur'], "\n")
print("id // attendu : 3 // recu :", karte['id'], "\n")
karte['post'] ("Nbr_PV 3", att_k)
print("post // attendu : nbr_pv = 3 // recu :", att_k['Nbr_PV'], "\n")
print("pre // attendu : false // recu :", karte['pre'] (att_k, cout_k, 3, att_k['liste_id'], 0), "\n")

att_k['Production_s'] ['Pierre'] = 5
print("pre // attendu : true // recu :", karte['pre'] (att_k, cout_k, 3, att_k['liste_id'], 0), "\n")



# def Init_Joueurs(Liste_Joueurs):
    # Nbr_j = input("Combien de joueurs etes-vous ? ")
    # for i in range(Nbr_j-1):
        # Joueurs_'i' = Joueurs
        # Liste_Joueurs.append(Joueurs_'i')