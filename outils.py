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
    
class Temps_propa:
    def __init__(self):
        self.res= {}

    def relation(self, utilisateur, suivi):
        if utilisateur not in self.res:
            self.res[utilisateur]= []
        self.res[utilisateur].append(suivi)
    
    def temps(self, source, cible):
        file=[(source, 0)]
        visite= set([source])

        while file:
            explorer, profondeur= file.pop(0)
            if explorer== cible:
                return profondeur*5
            
            for voisin in self.res.get(explorer,[]):
                if voisin not in visite:
                    visite.add(voisin)
                    file.append((voisin, profondeur+1))

        return -1    