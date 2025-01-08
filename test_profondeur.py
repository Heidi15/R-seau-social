from outils import parcours_profondeur

def lire_graphe(nom_fichier):
    """
    Lit un fichier de graphe et retourne la matrice d'adjacence correspondante.
    """
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
        
    # Lecture de l'en-tête
    nb_sommets = int(lignes[1])
    
    # Création de la matrice d'adjacence initialisée à 0
    matrice = [[0 for _ in range(nb_sommets)] for _ in range(nb_sommets)]
    
    # Lecture des arcs et remplissage de la matrice
    for ligne in lignes[nb_sommets+2:]:  # 
        if ligne.strip():  # Ignore les lignes vides
            source, destination = map(int, ligne.strip().split())
            matrice[source][destination] = 1
            
    return matrice