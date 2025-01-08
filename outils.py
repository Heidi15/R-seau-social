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

class Graphe:
    def charger_graphe(description, type_representation="matrice"):
        lignes = description.strip().split("\n")
        sommets = []
        aretes = []
        
        for ligne in lignes:
            ligne = ligne.strip()
            if not ligne:
                continue
            if "->" in ligne or "--" in ligne:  # C'est une arête
                parties = ligne.replace("->", " -> ").replace("--", " -- ").split()
                sommet1 = parties[0]
                sommet2 = parties[-1]
                if sommet1 not in sommets:
                    sommets.append(sommet1)
                if sommet2 not in sommets:
                    sommets.append(sommet2)
                aretes.append((sommet1, sommet2))
            else:  # C'est un sommet isolé
                if ligne not in sommets:
                    sommets.append(ligne)
        
        if type_representation == "matrice":
            n = len(sommets)
            matrice = [[0] * n for _ in range(n)]

            for arete in aretes:
                i = sommets.index(arete[0])
                j = sommets.index(arete[1])
                matrice[i][j] = 1
                if "--" in description:  # Graphe non orienté
                    matrice[j][i] = 1
                    
            return (sommets, matrice)
        
        else:
            adj = {sommet: [] for sommet in sommets}
            
            for arete in aretes:
                adj[arete[0]].append(arete[1])
                if "--" in description:  # Graphe non orienté
                    adj[arete[1]].append(arete[0])
                    
            return (sommets, adj)