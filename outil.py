def nombre_arcs_matrice_adjacence(matrice):
    
    count = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 1:
                count += 1
    return count



def nombre_arcs_liste_adjacence(liste):
    count = 0
    for voisins in liste:
        count += len(voisins)
    return count

