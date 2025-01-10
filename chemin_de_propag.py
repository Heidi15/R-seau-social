def chemin_minimum(graphe, source, destination):
    
    file = [source]  
    predecesseur = {source: None}  
    
    while file:
        personne_actuelle = file.pop(0)

        if personne_actuelle == destination:
            chemin = []
            while personne_actuelle is not None:
                chemin.append(personne_actuelle)
                personne_actuelle = predecesseur[personne_actuelle]
            return chemin[::-1]  

        for voisin in graphe.get(personne_actuelle, []):
            if voisin not in predecesseur:  
                file.append(voisin)
                predecesseur[voisin] = personne_actuelle


    return None
