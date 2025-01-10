from outils import nombre_aretes_matrice, nombre_aretes_liste

def test_nombre_aretes():
    print("=== Test nombre d'arêtes ===")
    # Test avec matrice d'adjacence
    matrice = [
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert nombre_aretes_matrice(matrice) == 2, "Le graphe devrait avoir 2 arêtes"
    
    # Test avec liste d'adjacence
    liste = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A']
    }
    assert nombre_aretes_liste(liste) == 2, "Le graphe devrait avoir 2 arêtes"
    print("Tests nombre d'arêtes OK")

if __name__ == "__main__":
    test_nombre_aretes()
    print("\nTous les tests sont passés avec succès!")    