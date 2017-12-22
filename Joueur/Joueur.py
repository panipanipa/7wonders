import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders' )
import attribut.attributs
import carte.carte
import Wonder.wonder as W

#definition de nos variables
attributs_acheteur = dict(attribut.attributs.Attributs)
attributs_vendeur = dict(attribut.attributs.Attributs)
res_a_acheter = dict(attribut.attributs.Ressources)

Liste_c=list()

#definition du type joueur : ce n'est qu'un ensemble d'attribut associé à une merveille et à une main
Joueur = dict ()
Joueur = {'attributs' : attribut.attributs.Attributs, \
          'merveille' : W.wonder, \
          'cartes' : Liste_c}

merveille = dict(W.wonder)

#fonction qui renvoie un type joueur si on lui donne une merveille (qu'on aura répartit au hasard)
def Init_Joueur(merveille) :
    JoueurI = dict(Joueur)
    JoueurI['attributs'] = attribut.attributs.init_attribut()
    JoueurI['merveille'] = merveille
    JoueurI['cartes'] = []
    return JoueurI

#fonction qui prend en argument des ressources et un joueur ou les acheter, elle renvoie un booléan disant si on peut les acheter
def ressource_achetable(attributs_vendeur, res_a_acheter):
    #on_cherche_xor = True
    for res, val in res_a_acheter.items() :
        prod_ac = attributs_vendeur['Production_s'][res]
        if val > prod_ac:
            mem = 10
            for res_possible in attributs_vendeur['Production_c']['Liste_ressources_possibles']:
                a = carte.cartes.differencier(res_a_acheter, res_possible)
                if a < mem:
                    mem = a
            if mem != 0 :
                return False
    return True

#orientation = droite ou gauche, partant du postulat que la ressource est achetable, celle-ci renvoie le montant qu'il faudra payer
def montant_a_payer(attributs_acheteur, res_a_acheter,orientation):
    montant = 0
    for res, val in res_a_acheter :
        if res in ["Papyrus","Verre","Tissu"] :
            montant += val * attributs_acheteur['prix_achat']['grise']
        elif orientation == "droite" :
            montant += val * attributs_acheteur['prix_achat']['marrondroite']
        else :
            montant += val * attributs_acheteur['prix_achat']['marrongauche']
    if montant > attributs_acheteur['Production_s']['Or'] :
        return -1
    else :
        return montant
    #cette fonction retourne le montant qu'aura à payer un joueur selon les ressources qu'il achète

def triger_achat_ressource(attributs_acheteur,attributs_vendeur, montant, ressources_a_ajouter) :
    attributs_acheteur['Production_s']['Or'] -= montant
    attributs_vendeur['Production_s']['Or'] += montant
    for res, val in ressources_a_ajouter :
        attributs_acheteur['Production_a'][res]+= val
    #cette fonction effectue l'echange d'argent et l'ajout des ressources achetées, il faut au préalable s'assurer que le joueur a l'argent

# demande est un string
# cle  puis le nombre voulu
def achat (attributs_acheteur, attributs_vendeur, demande, orientation):
    list_demande = demande.split(' ')
    cardinal = len(list_demande)
    i = 0
    offre = dict(attribut.attributs.Ressources)
    while i < cardinal:
        offre[list_demande[i]] = int(list_demande[i + 1])
        i += 2

    if ressource_achetable(attributs_vendeur, offre):
        prix = montant_a_payer(attributs_acheteur, offre, orientation)

        if prix > attributs_acheteur['Production_s']['Or']:
            triger_achat_ressource(attributs_acheteur, attributs_vendeur, prix, offre)
#



    #        if cartes_prod_xor != []:
    #            val-prod_ac = ressource_manquante
    #           cartes_prod_xor = attributs_vendeur['Production_c']
    #          while ressource_manquante != 0:
    #             for carte_xor in cartes_prod_xor :
    #                if len(carte_xor) == 2:
    #                   for ress_produite in carte_xor:
    #                      if ress_produite == res :
    #                         ressource_manquante -= 1
                                    
