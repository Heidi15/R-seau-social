from outils import Arc

def test_arc():
    # Test matrice d'adjacence
    matrice = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert Arc.nombre_arcs_matrice_adjacence(matrice) == 3
    
    # Test liste d'adjacence
    liste = [
        [1],       # sommet 0
        [0, 2],    # sommet 1
        [1]        # sommet 2
    ]
    assert Arc.nombre_arcs_liste_adjacence(liste) == 3

if __name__ == "__main__":
    test_arc()
    print("Tous les tests ont réussi.")