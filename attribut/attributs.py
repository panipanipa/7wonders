
#Production_simple : dictionnaire contenant toutes les ressources non xor présentes dans le jeu associé à un joueur
Ressources = dict ()
Ressources = {'Pierre' : 0, \
'Bois' : 0, \
'Argile' : 0, \
'Minerai' : 0, \
'Verre' : 0, \
'Papyrus' : 0, \
'Tissu' : 0, \
'Or' : 0}

Production_simple_exemple = {'Pierre' : 2, \
'Bois' : 0, \
'Argile' : 3, \
'Minerai' : 1, \
'Verre' : 0, \
'Papyrus' : 1, \
'Tissu' : 0, \
'Or' : 5}

Armee = dict()
Armee = {'PV1' : 0, \
         'PV3' : 0, \
         'PV5' : 0, \
         'PD' : 0, }

#Production_xor : dictionnaire contenant les ressources xor présentes chez les joueurs

Production_c = dict()
Production_c = {'JokerM': 0,
                'JokerG': 0,
                #elle contient des dict ressources
                'Liste_ressources_possibles': list()}
#JokerM et JokerG sont les ressources qui ont le plus de choix

#Production_xor_exemple = ["Bois Pierre","Pierre Bois"]

#Science : liste contenant la science math, ecriture et inginerie
Science = dict()
Science = {'Psm': 0, 'Pse': 0, 'Psi': 0}

Achat = dict()
Achat = {'marrondroite' : 2, 'grise' : 2, 'marrongauche' :2}

ID = list()


#attributs est le type contenant tout les variables associé à un joueur
#exemple : sa production
Attributs = dict()
Attributs = {'Nbr_c_b': 0,\
             'Nbr_c_m': 0,\
             'Nbr_c_g': 0,\
             'Nbr_c_r': 0,\
             'Nbr_c_v': 0,\
             'Nbr_c_j': 0,\
             'Nbr_c_vi': 0,\
             'Science': dict(Science),\
             'prix_achat': dict(Achat),\
             'Production_s': dict(Ressources),\
             'Production_c': dict(Production_c),\
             'Production_a': dict(Ressources),\
             'liste_id': list(ID),\
             'Nbr_PV': 0,\
             'Force' : 0, \
             'Armee' : dict(Armee)}

# creation d'une fonction pour creer un attributs
# probleme de referencement sinon pour les dictionnaire de dictionnaires

def init_attribut():
    res = dict(Attributs)
    res['Science'] = dict(Attributs['Science'])
    res['prix_achat'] = dict(Attributs['prix_achat'])
    res['Production_s'] = dict(Attributs['Production_s'])
    res['Production_c'] = dict(Attributs['Production_c'])
    res['Production_a'] = dict(Attributs['Production_a'])
    res['liste_id'] = list(Attributs['liste_id'])
    return res

def stringtoRessources(phrase):
    Resultat = dict(Ressources)
    if phrase == "":
        return Resultat
    else:
        info = phrase.split(' ')
        cardinal = len(info)
        i = 0

        while i < cardinal:
            Resultat[info[i]] = int(info[i + 1])
            i += 2
        return Resultat


