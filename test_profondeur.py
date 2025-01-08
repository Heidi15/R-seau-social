def parcours_profondeur(matrice_adjacence, sommet_depart):
    """
    Effectue un parcours en profondeur sur un graphe représenté par une matrice d'adjacence.

    Arguments :
    matrice_adjacence (list) : Matrice d'adjacence du graphe.
    sommet_depart (int) : Sommet de départ pour le parcours.

    Retourne :
    list : Liste des sommets visités.
    """
    visites = [False] * len(matrice_adjacence)  # Liste pour suivre les sommets visités
    resultat = []  # Liste des sommets dans l'ordre de visite
    
    pile = [sommet_depart]  # Utilisation d'une pile pour le parcours
    
    while pile:
        sommet = pile.pop()  # Récupère le dernier élément de la pile
        if not visites[sommet]:
            visites[sommet] = True  # Marque le sommet comme visité
            resultat.append(sommet)  # Ajoute le sommet au résultat
            # Ajoute les voisins non visités à la pile
            for voisin in range(len(matrice_adjacence[sommet]) - 1, -1, -1):
                if matrice_adjacence[sommet][voisin] == 1 and not visites[voisin]:
                    pile.append(voisin)
    
    return resultat