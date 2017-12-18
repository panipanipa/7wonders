import sys
sys.path.insert(1, '/home/tek/Desktop/7wonders/7wonders' )
import attribut.attributs
import carte.carte

attributs_acheteur = dict(attribut.attributs.Attributs)
attributs_vendeur = dict(attribut.attributs.Attributs)
res_a_acheter = dict(attribut.attributs.Ressources)

def ressource_achetable(attributs_vendeur, res_a_acheter):
    #on_cherche_xor = True
    for res, val in res_a_acheter.items :
        prod_ac = attributs_vendeur['Production_s'][res]
        if val > prod_ac:
            mem = 10
            for res_possible in attributs_vendeur.Liste_ressources_possibles:
                a = carte.cartes.differencier(res_a_acheter, res_possible)
                if a < mem:
                    mem = a
            if mem != 0 :
                return False
    return True

#on dit à la fonction ce qu'il achète ou)
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
    #cette fonction effectue l'echange d'argent et l'ajout des ressources achetées

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
                                    
