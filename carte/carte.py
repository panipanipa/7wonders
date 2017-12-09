import attribut.attributs
import os
os.chdir("/home/denis/PycharmProjects/7wonder/carte")
# faudra changer cette commande selon ton cas

# le but de ce programme est de lire dans un fichier les differentes informations
# 1 carte par ligne
# le separateur d'information est le ";" pour des reutilisations de code deja fait
# ben oui, je suis pour le recyclage

#fonction inutile si on utilise la librairie pandas mais c'est trop dur pour moi de m'en separer

def info_d(chaine):
    compteur = 0
    nom = ""
    nb_joueur = ""
    effet = ""
    cout = ""
    chainage = ""
    chainera = ""
    couleur = ""
    i = 0

    for i in chaine:

        if i == ';':
            compteur += 1
        elif compteur == 0:
            nom = nom + i
        elif compteur == 1:
            nb_joueur = i
        elif compteur == 2:
            effet = effet + i
        elif compteur == 3:
            cout = cout + i
        elif compteur == 4:
            chainage = chainage + i
        elif compteur == 5:
            chainera = chainera + i
        elif compteur == 6:
            couleur = couleur + i

    return [nom, nb_joueur, effet, cout, chainage, chainera, couleur]






liste_attribut = list();
#A1 attribut joueur gauche
A1=attribut
#A2 attribut du joueur jouant
A2=attribut
#A3 attribut du joueur de droite
A3=attribut
liste_attribut = [A1, A2, A3]


def Faut_il_faire_un_truc(Ressource_manquante):
    RAF = True
    for val in Ressource_manquante.values:
        if val != 0:
            RAF = False
    return RAF


# fonction qui prend les attributs, les modifie si l'achat est possible et retourne vrai ou sinon retourne faux
def Est_Achetable(Attribut_vendeur, Ressources_manquantes):
    for res, val in Ressources_manquantes:
        prod_ac = Attribut_vendeur['Production_s'][res]
        if val > prod_ac:
            Ressources_manquantes[res] = val - prod_ac
            print("il vous manque ", val - prod_ac, " ", res, )
        else:
            Ressources_manquantes[res] = 0

            # maintenant, on travaille uniquement avec les ressources manquantes et on vérifie si il faut allez utiliser les ressource xor

    RienAFaire = Faut_il_faire_un_truc(Ressources_manquantes)
    if not RienAFaire:
        cartes_prod_xor = Attribut_vendeur['Production_c']
        V = False
        Q = False
        while (not Q) and not RienAFaire and cartes_prod_xor != []:
            # on demande au joueur ce qu'il veut que ses cartes produisent en premier tant qu'il ne quitte pas et que ce n'est pas finit
            Ress_a_prio = input(
                "Vous pouvez acheter à une production diverse, quelle ressource voulez-vous qu'elle produise en priorité ? (ecrire en toute lettre), Q pour quitter")
            if Ress_a_prio == Q:
                Q = True
            else:
                # on crée une liste intermédiaire, que l'on va modifier selon nos besoins, en plus on passe d'abord par les 2 puis les 4
                for carte_xor in cartes_prod_xor:
                    if len(carte_xor) == 2:
                        for ress_produite in carte_xor:
                            if ress_produite == Ress_a_prio:
                                Ressources_manquantes[Ress_a_prio] -= 1
                                cartes_prod_xor.remove[carte_xor]
                    if Ressources_manquantes[Ress_a_prio] != 0:
                        for carte_xor in cartes_prod_xor:
                            if len(carte_xor) == 4:
                                Ressources_manquantes[Ress_a_prio] -= 1
                                cartes_prod_xor.remove[carte_xor]
        if Q:
            return False
        else:
            return True

#liste_carte a ete cree pour resoudre une erreur
#faut voir si on definit cette variable ici ou dans un autre package
liste_carte = list()


def Payer_Carte(liste_attribut):
    return

#effet est un string avec un espace délimittant la clé et son incrémentation
#at_joueur est un attribut associé avec un joueur
def Trigger_effet(effet, at_joueur):
    info = effet.split(' ')
    at_joueur[info[0]] += int(info[1])

def test_trigger(info, at_joueur):
    Trigger_effet(info, at_joueur)
    print(at_joueur['Bois'])

#fonction qui renvoie un boolean indiquant si la carte est chainable on non
def Est_chainable(nom_carte_qui_chaine, liste_carte):
    Resultat = False
    if nom_carte_qui_chaine != "":
        for c in liste_carte:
            if c['nom'] == nom_carte_qui_chaine:
                Resultat = True
    return Resultat

#fonction qui renvoie un boolean indiquant si la carte est chainable on non
def Est_chainable_id(id_qui_chaine, liste_id):
    Resultat = False
    if id_qui_chaine != 0:
        for c in liste_id:
            if c == id_qui_chaine:
                Resultat = True
    return Resultat

#cout est une variable définissant le cout d'une carte (a modifie pour chaque carte)
cout = ""


#fonction qui renvoie un boolean indiquant si les attributs passes en argument permettent de jouer la carte
#cout est une variable définissant le cout d'une carte (a modifie pour chaque carte)
#cout est un string contenant lees clefs des ressources et leur nombre requis avec " " comme separateur
#exemple : cout = "Bois 2 Pierre 2"
def Ressources_presente (attribut, cout):
    i = 0
    info_c = list()
    info_c = cout.split(' ')
    cardinal = len(info_c)
    Resultat = True
    while i < cardinal:
        Resultat = attribut['Production_s'][info_c[i]] >= int(info_c[i+1]) and Resultat
        i += 2
    return Resultat

#fonction qui renvoie le boolean indiquant si la carte a deja ete joue
def Est_deja_jouee(id, attribut):
    Resultat = False
    for c in attribut['liste_id']:
        if c == id:
            Resultat = True
    return Resultat



#definition de notre type carte
carte = dict()
carte = {'nom': " ",\

         #couleur est soit indeterminé(i) bleu(b) marron(m) grise(g) rouge(r) verte(v) jaune(j) violet(vi)
         'couleur': "i",\

         #entier associe a une carte pour la designer
         'id' : 0,\

         #fonction qui permet de savoir si la carte est jouable
         #'pre': (Ressources_presente or Est_chainable_id) and not Est_deja_jouee, \
         'pre': lambda att_k, cout_k , id_k, liste_id, id_c : \
             ( Ressources_presente(att_k, cout_k) or Est_chainable_id(id_c, liste_id)) \
             and not Est_deja_jouee(id_k, att_k), \

         #fonction appliquant l'effet de la carte
         'post':  Trigger_effet,\
         }

def Est_Jouable_prototype(liste_attribut, carte):

    # bool pour savoir si le joueur veut toujours jouer la carte
    Q = False
    # differents cas selon si la carte est chainable

    # on crée une dictionnaire de ressources manquantes, tant qu'il est pas égal à 0 on renvoie continue
    Ressources_manquante = attribut.attributs.Ressources
    # on parcourt notre liste de ressource à payer et leur nombre, on compare avec la production et on stocke dans ressource manquante
    for ress, val in carte.cout.items:
        prod_ac = liste_attribut[2]['Production_s'][ress]
        if val > prod_ac:
            Ressources_manquante[ress] = val - prod_ac
            print("il vous manque ", val - prod_ac, " ", ress, )
        else:
            Ressources_manquante[ress] = 0

            # maintenant, on travaille uniquement avec les ressources manquantes et on vérifie si il faut allez utiliser les ressource xor

    RienAFaire = Faut_il_faire_un_truc(Ressources_manquante)
    if not RienAFaire:
        cartes_prod_xor = liste_attribut[2]['Production_c']
        V = False
        Q = False
        while (not Q) and (not V) and not RienAFaire and cartes_prod_xor != []:
            # on demande au joueur ce qu'il veut que ses cartes produisent en premier tant qu'il ne quitte pas et que ce n'est pas finit
            Ress_a_prio = input(
                "Vous disposez d'au moins une carte production diverse, quelle ressource voulez-vous qu'elle produise en priorité ? (ecrire en toute lettre), Q pour quitter, V pour passer à l'étape d'achat")
            if Ress_a_prio == Q:
                Q = True
            elif Ress_a_prio == V:
                V = True
            else:
                # on crée une liste intermédiaire, que l'on va modifier selon nos besoins, en plus on passe d'abord par les 2 puis les 4
                for carte_xor in cartes_prod_xor:
                    if len(carte_xor) == 2:
                        for ress_produite in carte_xor:
                            if ress_produite == Ress_a_prio:
                                Ressources_manquante[Ress_a_prio] -= 1
                                cartes_prod_xor.remove[carte_xor]
                    if Ressources_manquante[Ress_a_prio] != 0:
                        for carte_xor in cartes_prod_xor:
                            if len(carte_xor) == 4:
                                Ressources_manquante[Ress_a_prio] -= 1
                                cartes_prod_xor.remove[carte_xor]
                RienAFaire = Faut_il_faire_un_truc


        if Q:
            return False
        elif RienAFaire:
            return True
        else:
            for (ress, val) in Ressources_manquante.items:
                if val != 0:
                    print("il vous manque", val, " ", ress)
            Q = False
            V = False
            Ress_achat_D = attribut.attributs.Ressources
            Ress_achat_G = attribut.attributs.Ressources
            cout_d = 0
            cout_g = 0
            while (not Q) and (not V):
                ress_achat = input("que voulez vous acheter à droite ? tapez en toute lettre, V pour valider, Q pour quitter")
                if ress_achat == Q:
                    return False
                elif ress_achat == V:
                    break
                Ress_achat_D[ress_achat] += 1

                if (ress_achat == "Papyrus" or ress_achat == "Tissu" or ress_achat == "Verre") :
                    cout_d += liste_attribut[2]['cout_achat']['grise']
                else:
                    cout_d += liste_attribut[2]['cout_achat']['marrondroite']

            while (not Q) and (not V):
                ress_achat = input("que voulez vous acheter à gauche ? tapez en toute lettre, V pour valider, Q pour quitter")
                if ress_achat == Q:
                    return False
                elif ress_achat == V:
                    break
                Ress_achat_G[ress_achat] += 1

                if (ress_achat == "Papyrus" or ress_achat == "Tissu" or ress_achat == "Verre"):
                    cout_g += liste_attribut[2]['cout_achat']['grise']
                else:
                    cout_g += liste_attribut[2]['cout_achat']['marrongauche']

            A = Est_Achetable(liste_attribut[1], Ress_achat_G)
            B = Est_Achetable(liste_attribut[3], Ress_achat_D)
            if A and B:
                cout_tot = cout_g + cout_d
                if cout_tot <= liste_attribut[2]['Production_s']['Or']:
                    liste_attribut[2]['Production_s']['Or'] -= cout_tot
                    liste_attribut[1]['Production_s']['Or'] += cout_g
                    liste_attribut[3]['Production_s']['Or'] += cout_d
                    return True
                else:
                    return False
            else:
                return False
    else:
        return True





