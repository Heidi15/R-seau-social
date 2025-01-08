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
    
class Influenceur:
    def plus_grands_influenceurs(reseau):
        """
        Identifie la/les personne(s) la/les plus suivie(s) dans le réseau.
        
        Args:
            reseau (dict): Dictionnaire avec comme clés les personnes et comme valeurs 
                        les listes des personnes qu'elles suivent
        
        Returns:
            list: Liste des personnes ayant le plus grand nombre de followers
        """
        # Compter les followers pour chaque personne
        nb_followers = {}
        
        # Initialiser le compteur pour chaque personne du réseau
        for personne in reseau:
            nb_followers[personne] = 0
        
        # Compter les followers
        for personne, suivis in reseau.items():
            for suivi in suivis:
                if suivi in nb_followers:
                    nb_followers[suivi] += 1
        
        # Trouver le nombre maximum de followers
        max_followers = 0
        if nb_followers:
            max_followers = max(nb_followers.values())
        
        # Identifier toutes les personnes ayant ce nombre maximum de followers
        influenceurs = [
            personne for personne, followers in nb_followers.items()
            if followers == max_followers
        ]
        
        return influenceurs