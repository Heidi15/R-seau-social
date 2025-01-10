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
    
class Communauté: 
    def est_une_seule_communauté(matrice_adjacence):
        def dfs(sommet, visites):
            """Effectue un parcours en profondeur à partir d'un sommet donné."""
        visites[sommet] = True
        for voisin, est_adjacent in enumerate(matrice_adjacence[sommet]):
            if est_adjacent == 1 and not visites[voisin]:
                dfs(voisin, visites)

        n = len(matrice_adjacence)
        visites = [False] * n
        dfs(0, visites)

        return all(visites)   