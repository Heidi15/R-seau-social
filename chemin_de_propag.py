from collections import deque

def chemin_minimum(reseau, source, cible):
    

    file = deque([(source, [source])])  
    
    visites = set()
    
    while file:
        personne_actuelle, chemin_actuel = file.popleft()
        
        
        if personne_actuelle == cible:
            return chemin_actuel
        
        
        visites.add(personne_actuelle)


        for voisin in reseau.get(personne_actuelle, []):
            if voisin not in visites:
                file.append((voisin, chemin_actuel + [voisin]))
    
    
    return []


if __name__ == "__main__":
   
    reseau = {
        "Alice": ["Bob", "Carol"],
        "Bob": ["Diane"],
        "Carol": ["Eve", "Diane"],
        "Diane": ["Eve"],
        "Eve": []
    }
    
   
    source = "Alice"
    cible = "Eve"
    
    chemin = chemin_minimum(reseau, source, cible)
    print(f"Le chemin minimum de {source} à {cible} est : {chemin}")
