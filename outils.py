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
    
class Largeur:
    def creer_matrice_adjacence(nb_sommets, arcs):
        """
        Crée une matrice d'adjacence à partir du nombre de sommets et de la liste des arcs
        """
        matrice = [[0 for _ in range(nb_sommets)] for _ in range(nb_sommets)]
        for depart, arrivee in arcs:
            matrice[depart][arrivee] = 1
        return matrice

    def parcours_largeur(matrice_adjacence, sommet_depart):
            """
            Effectue un parcours en largeur du graphe à partir d'un sommet donné
            
            Args:
                matrice_adjacence (list): Matrice d'adjacence du graphe
                sommet_depart (int): Sommet de départ du parcours
                
            Returns:
                list: Liste des sommets visités dans l'ordre du parcours
            """
            nb_sommets = len(matrice_adjacence)
            visites = []
            marques = [False] * nb_sommets
            
            # Création d'une file pour le parcours en largeur
            file = File()
            
            # On commence par le sommet de départ
            file.enfiler(sommet_depart)
            marques[sommet_depart] = True
            
            while not file.est_vide():
                sommet_courant = file.defiler()
                visites.append(sommet_courant)
                
                # On parcourt tous les sommets adjacents
                for sommet_suivant in range(nb_sommets):
                    if matrice_adjacence[sommet_courant][sommet_suivant] == 1 and not marques[sommet_suivant]:
                        file.enfiler(sommet_suivant)
                        marques[sommet_suivant] = True
                        
            return visites