import attribut.attributs
import carte.cartes

attributs_acheteur = dict(attribut.attributs.Attributs)
attributs_vendeur = dict(attribut.attributs.Attributs)
res_a_acheter = dict(attribut.attributs.Ressources)
def acheter_ressources(res_a_acheter, attributs_acheteur, attributs_vendeurs):
    on_cherche_xor = True
    for res, val in res_a_acheter :
        prod_ac = attributs_vendeur['Production_s'][res]
        if val > prod_ac :
            if cartes_prod_xor != []:
                val-prod_ac = ressource_manquante
                cartes_prod_xor = attributs_vendeur['Production_c']
                while ressource_manquante != 0:
                    for carte_xor in cartes_prod_xor :
                        if len(carte_xor) == 2:
                            for ress_produite in carte_xor:
                                if ress_produite == res :
                                    ressource_manquante -= 1
                                    
