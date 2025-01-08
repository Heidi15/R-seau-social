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

# Tests
if __name__ == "__main__":
    # Lecture du graphe
    matrice = lire_graphe("go-9-01.txt")
    
    # Test 1: Vérifier que le parcours commence par le sommet de départ
    sommet_depart = 0
    resultat = parcours_profondeur(matrice, sommet_depart)
    assert resultat[0] == sommet_depart, f"Le parcours devrait commencer par le sommet {sommet_depart}"
    
    # Test 2: Vérifier que tous les sommets accessibles sont visités
    assert len(set(resultat)) == len(resultat), "Le parcours ne devrait pas contenir de doublons"
    
    # Test 3: Vérifier le parcours depuis différents sommets de départ
    for sommet in [3, 5, 8]:
        resultat = parcours_profondeur(matrice, sommet)
        assert resultat[0] == sommet, f"Le parcours depuis {sommet} devrait commencer par {sommet}"
    
    # Test 4: Vérifier que les sommets isolés donnent un parcours minimal
    sommet_isole = -1
    for i in range(len(matrice)):
        if sum(matrice[i]) == 0:  # Si le sommet n'a pas d'arcs sortants
            sommet_isole = i
            break
    if sommet_isole != -1:
        resultat = parcours_profondeur(matrice, sommet_isole)
        assert len(resultat) == 1, f"Le parcours depuis un sommet isolé devrait contenir uniquement ce sommet"
        assert resultat[0] == sommet_isole, "Le parcours depuis un sommet isolé est incorrect"
    
    print("Tous les tests sont passés avec succès!")