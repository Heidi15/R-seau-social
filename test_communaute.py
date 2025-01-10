from outils import une_seule_communaute

def test_communaute():
    print("=== Test communauté ===")
    # Test avec un graphe connexe
    sommets = ['A', 'B', 'C']
    matrice_connexe = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    assert une_seule_communaute(sommets, matrice_connexe) == True, "Le graphe devrait former une seule communauté"
    
    # Test avec un graphe non connexe
    matrice_non_connexe = [
        [0, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert une_seule_communaute(sommets, matrice_non_connexe) == False, "Le graphe ne devrait pas former une seule communauté"
    print("Tests communauté OK")

if __name__ == "__main__":
    test_communaute()
    print("\nTous les tests sont passés avec succès!") 