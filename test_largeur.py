if __name__ == "__main__":
    """
    Tests pour la fonction parcours_largeur.
    """
    # Exemple de graphe représenté par une matrice d'adjacence
    # 0 --- 1
    # |     |
    # 2 --- 3
    matrice = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    # Test 1 : Parcours à partir du sommet 0
    resultat = parcours_largeur(matrice, 0)
    assert resultat == [0, 1, 2, 3], f"Échec  test 1 : {resultat}"

    # Test 2 : Parcours à partir du sommet 2
    resultat = parcours_largeur(matrice, 2)
    assert resultat == [2, 0, 3, 1], f"Échec  test 2 : {resultat}"

    print("TEST RÉUSSIES !")
