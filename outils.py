class Pile:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def empiler(self, element):
        self.elements.append(element)
    
    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de dépiler une pile vide")
        return self.elements.pop()
    
    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.elements[-1]

class File:
    def __init__(self):
        self.elements = []
    
    def est_vide(self):
        return len(self.elements) == 0
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if self.est_vide():
            raise IndexError("Impossible de défiler une file vide")
        return self.elements.pop(0)
    
    def premier(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        return self.elements[0]
    
class Chemin_Propagation:
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