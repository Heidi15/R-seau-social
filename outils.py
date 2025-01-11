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
    """
    Compte le nombre d'arêtes dans un graphe non orienté représenté par une matrice d'adjacence
    
    Args:
        matrice: Matrice d'adjacence du graphe
    
    Returns:
        Nombre d'arêtes dans le graphe
    """
    count = 0
    for i in range(len(matrice)):
        for j in range(i + 1, len(matrice)):  # Compte uniquement le triangle supérieur
            if matrice[i][j] == 1:
                count += 1
    return count

def nombre_aretes_liste(liste_adj):
    """
    Compte le nombre d'arêtes dans un graphe non orienté représenté par une liste d'adjacence
    
    Args:
        liste_adj: Liste d'adjacence du graphe
    
    Returns:
        Nombre d'arêtes dans le graphe
    """
    count = 0
    for sommet, voisins in liste_adj.items():
        count += len(voisins)
    return count // 2  # Divise par 2 car chaque arête est comptée deux fois

def nombre_arcs_matrice(matrice):
    """
    Compte le nombre d'arcs dans un graphe orienté représenté par une matrice d'adjacence
    
    Args:
        matrice: Matrice d'adjacence du graphe
    
    Returns:
        Nombre d'arcs dans le graphe
    """
    count = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] == 1:
                count += 1
    return count

def nombre_arcs_liste(liste_adj):
    """
    Compte le nombre d'arcs dans un graphe orienté représenté par une liste d'adjacence
    
    Args:
        liste_adj: Liste d'adjacence du graphe
    
    Returns:
        Nombre d'arcs dans le graphe
    """
    return sum(len(voisins) for voisins in liste_adj.values())

def charger_graphe(description, type_representation="matrice"):
    """
    Charge un graphe à partir d'une description textuelle
    
    Args:
        description: Description textuelle du graphe
        type_representation: Type de représentation souhaité ("matrice" ou "liste")
    
    Returns:
        Tuple contenant la liste des sommets et la représentation du graphe choisie
    """
    lignes = description.strip().split("\n")
    est_oriente = "ORIENTE" in lignes[0]
    nb_sommets = int(lignes[1].split()[0])
    
    # Extraction des sommets
    sommets = []
    current_line = 2
    for _ in range(nb_sommets):
        sommets.append(lignes[current_line].strip())
        current_line += 1
    
    # Passe la ligne Arcs/Aretes
    nb_liens = int(lignes[current_line].split()[0])
    current_line += 1
    
    if type_representation == "matrice":
        # Initialisation de la matrice d'adjacence
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
        # Initialisation de la liste d'adjacence
        liste_adj = {s: [] for s in sommets}
        
        # Remplissage de la liste d'adjacence
        for i in range(nb_liens):
            s1, s2 = lignes[current_line + i].strip().split()
            liste_adj[s1].append(s2)
            if not est_oriente:
                liste_adj[s2].append(s1)
        
        return (sommets, liste_adj)

def parcours_profondeur(matrice_adj, sommet_depart):
    """
    Réalise un parcours en profondeur du graphe
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
        sommet_depart: Indice du sommet de départ
    
    Returns:
        Liste des sommets visités dans l'ordre du parcours
    """
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
    """
    Réalise un parcours en largeur du graphe
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
        sommet_depart: Indice du sommet de départ
    
    Returns:
        Liste des sommets visités dans l'ordre du parcours
    """
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
    """
    Vérifie si le réseau forme une seule communauté
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
    
    Returns:
        True si le graphe forme une seule communauté, False sinon
    """
    if len(matrice_adj) == 0:
        return True
    visites = parcours_largeur(matrice_adj, 0)
    return len(visites) == len(matrice_adj)

def plus_grands_influenceurs(matrice_adj, sommets):
    """
    Trouve les utilisateurs les plus influents du réseau
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
        sommets: Liste des noms des sommets
    
    Returns:
        Liste des noms des plus grands influenceurs
    """
    nb_followers = [sum(matrice_adj[j][i] for j in range(len(matrice_adj))) 
                   for i in range(len(matrice_adj))]
    max_followers = max(nb_followers)
    return [sommets[i] for i in range(len(sommets)) 
            if nb_followers[i] == max_followers]

def temps_propagation(matrice_adj, source, cible):
    """
    Calcule le temps de propagation entre deux utilisateurs
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
        source: Indice du sommet source
        cible: Indice du sommet cible
        temps_propagation_unitaire: Temps de propagation entre deux sommets adjacents
    
    Returns:
        Temps de propagation ou -1 si aucun chemin n'existe
    """
    chemin = parcours_largeur(matrice_adj, source)
    if cible not in chemin:
        return -1
    return chemin.index(cible) * 5  # 5 minutes par étape (on peut modifier le temps)

def chemin_propagation(matrice_adj, sommets, source, destination):
    """
    Trouve le chemin de propagation le plus court
    
    Args:
        matrice_adj: Matrice d'adjacence du graphe
        sommets: Liste des noms des sommets
        source: Nom du sommet source
        destination: Nom du sommet destination
    
    Returns:
        Liste des noms des sommets formant le chemin le plus court ou None si aucun chemin n'existe
    """
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
        """Initialise le générateur de graphe"""
        self.graphe = {}
        
    def creation_graphe(self, oriente, nb_sommets, min_deg, max_deg, nb_communautes, distance_max=None):
        """
        Crée un graphe aléatoire respectant les contraintes données.
        
        Args:
            oriente: True si le graphe est orienté, False sinon
            nb_sommets: Nombre total de sommets dans le graphe
            min_deg: Degré minimum de chaque sommet
            max_deg: Degré maximum de chaque sommet
            nb_communautes: Nombre de communautés distinctes à créer
            distance_max: Distance maximale entre deux sommets (optionnel)
        
        Returns:
            Dictionnaire représentant le graphe sous forme de liste d'adjacence
        
        Raises:
            ValueError: Si les paramètres sont incohérents
                (ex: min_deg > max_deg ou nb_communautes > nb_sommets)
        """
        import random
        
        self.graphe = {i: [] for i in range(nb_sommets)}
        taille_communaute = nb_sommets // nb_communautes
        
        # Création des communautés
        for comm in range(nb_communautes):
            debut = comm * taille_communaute
            fin = (comm + 1) * taille_communaute if comm < nb_communautes - 1 else nb_sommets
            
            # Connexions dans la communauté
            for i in range(debut, fin):
                while len(self.graphe[i]) < min_deg:
                    j = random.randint(debut, fin-1)
                    if i != j and j not in self.graphe[i]:
                        self.graphe[i].append(j)
                        if not oriente:
                            self.graphe[j].append(i)
        
        # Ajout de connexions aléatoires jusqu'au degré maximum
        for i in range(nb_sommets):
            while len(self.graphe[i]) < max_deg:
                j = random.randint(0, nb_sommets-1)
                if i != j and j not in self.graphe[i]:
                    self.graphe[i].append(j)
                    if not oriente:
                        self.graphe[j].append(i)
        
        return self.graphe
    
    def enregistrer_graphe(self, fichier, oriente=True):
        """
        Sauvegarde le graphe dans un fichier texte au format spécifié.
        
        Le format du fichier est le suivant:
        - Première ligne: "GRAPHE ORIENTE" ou "GRAPHE NON ORIENTE"
        - Deuxième ligne: nombre de sommets suivi de "SOMMETS"
        - Une ligne par sommet avec son identifiant
        - Une ligne avec le nombre d'arcs/arêtes suivi de "ARCS" ou "ARETES"
        - Une ligne par arc/arête avec les deux sommets concernés
        
        Args:
            fichier: Chemin du fichier de sortie
            oriente: True si le graphe est orienté, False sinon
        
        Raises:
            IOError: Si l'écriture dans le fichier échoue
        """
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