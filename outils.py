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
    def __init__(self, matrice):
        self.matrice= matrice
    
    def aretesmatrice (self):
        if self.matrice:
            count= 0
            for i in range (len(self.matrice)):
                for ii in range (i+1, len(self.matrice)):
                    if self.matrice [i][ii]:
                        count+=1
            return count

    def __init__(self, liste):
        self.liste= liste
    
    def aretesliste (self):
        if self.liste:
            count= 0
            for i in range (len(self.liste)):
                for ii in range (len(self.liste)):
                    if self.liste[i]< self.liste[ii]:
                        count+=1
            return count