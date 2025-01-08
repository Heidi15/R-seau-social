from outils import File, parcours_largeur, creer_matrice_adjacence

def tester_parcours_largeur():
    # Création du graphe à partir des données de go-9-01.txt
    arcs = [
        (0, 1), (0, 3), (1, 4), (1, 6), (1, 8),
        (2, 4), (2, 5), (2, 6), (3, 4), (3, 7),
        (4, 1), (4, 5), (4, 6), (4, 7), (5, 0),
        (5, 1), (5, 8), (6, 8), (7, 2), (8, 1),
        (8, 2)
    ]
    nb_sommets = 9
    matrice = creer_matrice_adjacence(nb_sommets, arcs)

    # Test 1: Parcours depuis le sommet 0
    print("Test 1: Parcours depuis le sommet 0")
    resultat = parcours_largeur(matrice, 0)
    assert resultat[0] == 0, "Le premier sommet visité doit être 0"
    assert 1 in resultat[1:3], "Le sommet 1 doit être parmi les premiers voisins visités"
    assert 3 in resultat[1:3], "Le sommet 3 doit être parmi les premiers voisins visités"
    print("Test 1 réussi!")

    # Test 2: Vérification que tous les sommets sont visités
    print("\nTest 2: Vérification du nombre total de sommets visités")
    assert len(resultat) == nb_sommets, f"Tous les sommets doivent être visités (attendu: {nb_sommets}, obtenu: {len(resultat)})"
    assert len(set(resultat)) == nb_sommets, "Chaque sommet doit être visité une seule fois"
    print("Test 2 réussi!")

    # Test 3: Test avec le sommet 5 comme point de départ
    print("\nTest 3: Parcours depuis le sommet 5")
    resultat_5 = parcours_largeur(matrice, 5)
    assert resultat_5[0] == 5, "Le premier sommet visité doit être 5"
    assert 0 in resultat_5[1:4], "Le sommet 0 doit être parmi les premiers voisins visités"
    assert 1 in resultat_5[1:4], "Le sommet 1 doit être parmi les premiers voisins visités"
    assert 8 in resultat_5[1:4], "Le sommet 8 doit être parmi les premiers voisins visités"
    print("Test 3 réussi!")

    # Test 4: Test avec un graphe vide
    print("\nTest 4: Test avec un graphe vide")
    matrice_vide = creer_matrice_adjacence(1, [])
    resultat_vide = parcours_largeur(matrice_vide, 0)
    assert resultat_vide == [0], "Pour un graphe à un sommet, le résultat doit être [0]"
    print("Test 4 réussi!")

    print("\nTous les tests ont réussi!")

if __name__ == '__main__':
    tester_parcours_largeur()