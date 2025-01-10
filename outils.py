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

def nombre_aretes_matrice(matrice):
    count = 0
    for i in range(len(matrice)):
        for j in range(i + 1, len(matrice)):  # Compte uniquement le triangle supérieur
            if matrice[i][j] == 1:
                count += 1
    return count

def nombre_aretes_liste(liste_adj):
    count = 0
    for sommet, voisins in liste_adj.items():
        count += len(voisins)
    return count // 2  # Divise par 2 car chaque arête est comptée deux fois

def nombre_arcs_matrice(matrice):
    count = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                count += 1
    return count

def nombre_arcs_liste(liste_adj):
    return sum(len(voisins) for voisins in liste_adj.values())

def charger_graphe(description, type_representation="matrice"):
    lignes = description.strip().split("\n")
    est_oriente = "ORIENTE" in lignes[0]
    nb_sommets = int(lignes[1].split()[0])
    
    sommets = []
    current_line = 2
    for _ in range(nb_sommets):
        sommets.append(lignes[current_line].strip())
        current_line += 1
    
    # Passe la ligne Arcs/Aretes
    nb_liens = int(lignes[current_line].split()[0])
    current_line += 1
    
    if type_representation == "matrice":
        matrice = [[0] * nb_sommets for _ in range(nb_sommets)]
        
        # Remplissage de la matrice
        for i in range(nb_liens):
            s1, s2 = lignes[current_line + i].strip().split()
            idx1 = sommets.index(s1)
            idx2 = sommets.index(s2)
            matrice[idx1][idx2] = 1
            if not est_oriente:
                matrice[idx2][idx1] = 1
        
        return (sommets, matrice)
    else:
        liste_adj = {s: [] for s in sommets}
        
        for i in range(nb_liens):
            s1, s2 = lignes[current_line + i].strip().split()
            liste_adj[s1].append(s2)
            if not est_oriente:
                liste_adj[s2].append(s1)
        
        return (sommets, liste_adj)

def parcours_profondeur(matrice_adj, sommet_depart):
    n = len(matrice_adj)
    visites = [False] * n
    resultat = []
    
    def dfs_recursif(sommet):
        visites[sommet] = True
        resultat.append(sommet)
        for voisin in range(n):
            if matrice_adj[sommet][voisin] == 1 and not visites[voisin]:
                dfs_recursif(voisin)
    
    dfs_recursif(sommet_depart)
    return resultat

def parcours_largeur(matrice_adj, sommet_depart):
    n = len(matrice_adj)
    visites = [False] * n
    resultat = []
    file = File()
    
    visites[sommet_depart] = True
    file.enfiler(sommet_depart)
    resultat.append(sommet_depart)
    
    while not file.est_vide():
        sommet = file.defiler()
        for voisin in range(n):
            if matrice_adj[sommet][voisin] == 1 and not visites[voisin]:
                visites[voisin] = True
                file.enfiler(voisin)
                resultat.append(voisin)
    
    return resultat

def une_seule_communaute(matrice_adj):
    if len(matrice_adj) == 0:
        return True
    visites = parcours_largeur(matrice_adj, 0)
    return len(visites) == len(matrice_adj)

def plus_grands_influenceurs(matrice_adj, sommets):
    nb_followers = [sum(matrice_adj[j][i] for j in range(len(matrice_adj))) 
                   for i in range(len(matrice_adj))]
    max_followers = max(nb_followers)
    return [sommets[i] for i in range(len(sommets)) 
            if nb_followers[i] == max_followers]

def temps_propagation(matrice_adj, source, cible):
    chemin = parcours_largeur(matrice_adj, source)
    if cible not in chemin:
        return -1
    return chemin.index(cible) * 5  # 5 minutes par étape (on peut modifier le temps)

def chemin_propagation(matrice_adj, sommets, source, destination):
    file = File()
    source_idx = sommets.index(source)
    dest_idx = sommets.index(destination)
    n = len(matrice_adj)
    
    predecesseur = [-1] * n
    file.enfiler(source_idx)
    
    while not file.est_vide():
        sommet = file.defiler()
        if sommet == dest_idx:
            break
            
        for voisin in range(n):
            if matrice_adj[sommet][voisin] == 1 and predecesseur[voisin] == -1:
                predecesseur[voisin] = sommet
                file.enfiler(voisin)
    
    if predecesseur[dest_idx] == -1:
        return None
    
    chemin = []
    sommet = dest_idx
    while sommet != -1:
        chemin.append(sommets[sommet])
        sommet = predecesseur[sommet]
    
    return chemin[::-1]

class Generation_Graphe:
    def __init__(self):
        self.graphe = {}
        
    def creation_graphe(self, oriente, nb_sommets, min_deg, max_deg, nb_communautes, distance_max=None):
        import random
        
        self.graphe = {i: [] for i in range(nb_sommets)}
        taille_communaute = nb_sommets // nb_communautes
        
        # Création des communautés
        for comm in range(nb_communautes):
            debut = comm * taille_communaute
            fin = (comm + 1) * taille_communaute if comm < nb_communautes - 1 else nb_sommets
            
            for i in range(debut, fin):
                while len(self.graphe[i]) < min_deg:
                    j = random.randint(debut, fin-1)
                    if i != j and j not in self.graphe[i]:
                        self.graphe[i].append(j)
                        if not oriente:
                            self.graphe[j].append(i)
        
        for i in range(nb_sommets):
            while len(self.graphe[i]) < max_deg:
                j = random.randint(0, nb_sommets-1)
                if i != j and j not in self.graphe[i]:
                    self.graphe[i].append(j)
                    if not oriente:
                        self.graphe[j].append(i)
        
        return self.graphe
    
    def enregistrer_graphe(self, fichier, oriente=True):
        with open(fichier, 'w') as f:
            f.write("GRAPHE ORIENTE\n" if oriente else "GRAPHE NON ORIENTE\n")
            f.write(f"{len(self.graphe)} SOMMETS\n")
            
            for i in range(len(self.graphe)):
                f.write(f"{i}\n")
            
            arcs = []
            for sommet, voisins in self.graphe.items():
                for voisin in voisins:
                    arcs.append(f"{sommet} {voisin}")
            
            f.write(f"{len(arcs)} {'ARCS' if oriente else 'ARETES'}\n")
            for arc in arcs:
                f.write(f"{arc}\n")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 7:
        print("Usage: python outils.py nb_sommets min_deg max_deg oriente nb_communautes fichier_sortie")
        sys.exit(1)
    
    nb_sommets = int(sys.argv[1])
    min_deg = int(sys.argv[2])
    max_deg = int(sys.argv[3])
    oriente = sys.argv[4].lower() == "true"
    nb_communautes = int(sys.argv[5])
    fichier_sortie = sys.argv[6]
    
    generateur = Generation_Graphe()
    generateur.creation_graphe(oriente, nb_sommets, min_deg, max_deg, nb_communautes)
    generateur.enregistrer_graphe(fichier_sortie, oriente)
    print(f"Graphe généré et sauvegardé dans {fichier_sortie}")