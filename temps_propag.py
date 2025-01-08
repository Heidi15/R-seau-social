class reseauso:
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