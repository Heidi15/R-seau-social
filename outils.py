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

class Profondeur:
   def parcours_profondeur(matrice_adj, sommet_depart):
        """
        Réalise un parcours en profondeur d'un graphe orienté à partir d'un sommet donné.
        
        Args:
            matrice_adj (list): Matrice d'adjacence du graphe
            sommet_depart (int): Sommet de départ du parcours
            
        Returns:
            list: Liste des sommets visités dans l'ordre du parcours
        """
        n = len(matrice_adj)  # nombre de sommets
        visites = [False] * n  # tableau pour marquer les sommets visités
        sommets_visites = []  # liste pour stocker l'ordre de visite
        pile = Pile()  # utilisation de la classe Pile
        
        # On commence par le sommet de départ
        pile.empiler(sommet_depart)
        
        while not pile.est_vide():
            sommet = pile.depiler()
            
            if not visites[sommet]:
                # Marquer le sommet comme visité et l'ajouter à la liste
                visites[sommet] = True
                sommets_visites.append(sommet)
                
                # Parcourir les voisins dans l'ordre inverse pour respecter l'ordre naturel car on utilise une pile
                for voisin in range(n-1, -1, -1):
                    if matrice_adj[sommet][voisin] == 1 and not visites[voisin]:
                        pile.empiler(voisin)
        
        return sommets_visites