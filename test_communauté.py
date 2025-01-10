from outils import est_une_seule_communauté

def test_est_une_seule_communauté():    
    matrice1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    assert est_une_seule_communauté(matrice1) == True

    matrice2 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    assert est_une_seule_communauté(matrice2) == False
    print("Tests réussies !")

if __name__ == "__main__":
    test_est_une_seule_communauté()
