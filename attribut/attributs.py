
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

#Production_xor : dictionnaire contenant les ressources xor présentes chez les joueurs
Production_xor = list ()
Production_xor = []
Production_xor_exemple = [("Bois","Argile"), ("Bois","Pierre","Argile","Minerai")]

#Science : liste contenant la science math, ecriture et inginerie
Science = dict()
Science = {'Psm': 0, 'Pse': 0, 'Psi': 0}

Achat = dict()
Achat = {'marrondroite' : 2, 'grise' : 2, 'marrongauche' :2}


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
             'Production_c': list(Production_xor),\
             'Production_a': dict(Ressources),\
             'liste_id': list(), \
             'Nbr_PV': 0}
