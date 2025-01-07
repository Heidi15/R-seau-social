if __name__ == "__main__":
    
    
    matrice = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]

    resultat = parcours_largeur(matrice, 0)
    assert resultat == [0, 1, 2, 3], f"Échec  test 1 : {resultat}"

    resultat = parcours_largeur(matrice, 2)
    assert resultat == [2, 0, 3, 1], f"Échec  test 2 : {resultat}"

    print("TEST RÉUSSIES !")
