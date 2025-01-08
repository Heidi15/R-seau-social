def parcours_largeur(matrice_adjacence, sommet_depart):
    
  
    if sommet_depart < 0 or sommet_depart >= len(matrice_adjacence):
        raise ValueError("Le sommet de départ est invalide.")

    visites = [] 
    marqués = [False] * len(matrice_adjacence)  

    marqués[sommet_depart] = True

    while file:
        sommet_courant = file.pop(0)  
        visites.append(sommet_courant)  

    
        for voisin, est_adjacent in enumerate(matrice_adjacence[sommet_courant]):
            if est_adjacent and not marqués[voisin]:  
                file.append(voisin)  
                marqués[voisin] = True  
    return visites
