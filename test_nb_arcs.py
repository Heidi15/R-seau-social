from outils import nombre_arcs_matrice, nombre_arcs_liste

def test_nombre_arcs():
    print("=== Test nombre d'arcs ===")
    # Test avec matrice d'adjacence
    matrice = [
        [0, 1, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
    assert nombre_arcs_matrice(matrice) == 4, "Le graphe devrait avoir 4 arcs"
    
    # Test avec liste d'adjacence
    liste = {
        'A': ['B', 'C'],
        'B': ['C'],
        'C': ['A']
    }
    assert nombre_arcs_liste(liste) == 4, "Le graphe devrait avoir 4 arcs"
    print("Tests nombre d'arcs OK")