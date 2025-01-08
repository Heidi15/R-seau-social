class File:
    def __init__(self):
        self.elements = []
    
    def enfiler(self, element):
        self.elements.append(element)
    
    def defiler(self):
        if not self.est_vide():
            return self.elements.pop(0)
        raise IndexError("File vide")
    
    def est_vide(self):
        return len(self.elements) == 0

class Pile:
    def __init__(self):
        self.elements = []
    
    def empiler(self, element):
        self.elements.append(element)
    
    def depiler(self):
        if not self.est_vide():
            return self.elements.pop()
        raise IndexError("Pile vide")
    
    def est_vide(self):
        return len(self.elements) == 0