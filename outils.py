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
    
class Aretes:
    def __init__(self, matrice, liste):
        self.matrice= matrice
        self.liste= liste
    
    def aretesmatrice (self):
        if self.matrice:
            count= 0
            for i in range (len(self.matrice)):
                for ii in range (i+1, len(self.matrice)):
                    if self.matrice [i][ii]:
                        count+=1
            return count
    
    def aretesliste (self):
            count= 0
            for i in self.liste:
                count+= 1
            return count 