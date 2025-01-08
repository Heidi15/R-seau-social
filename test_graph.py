def test_charger_graphe():
    # Test 1: Graphe orienté simple avec matrice d'adjacence
    description1 = """
    A -> B
    B -> C
    C -> A
    """
    sommets1, matrice1 = charger_graphe(description1, "matrice")
    assert sommets1 == ['A', 'B', 'C']
    assert matrice1 == [
        [0, 1, 0],
        [0, 0, 1],
        [1, 0, 0]
    ]
    
    # Test 2: Même graphe avec liste d'adjacence
    sommets2, adj2 = charger_graphe(description1, "liste")
    assert sommets2 == ['A', 'B', 'C']
    assert adj2 == {'A': ['B'], 'B': ['C'], 'C': ['A']}
    
    # Test 3: Graphe non orienté avec matrice d'adjacence
    description2 = """
    A -- B
    B -- C
    """
    sommets3, matrice3 = charger_graphe(description2, "matrice")
    assert sommets3 == ['A', 'B', 'C']
    assert matrice3 == [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    
    # Test 4: Graphe avec sommet isolé
    description3 = """
    A -> B
    C
    """
    sommets4, adj4 = charger_graphe(description3, "liste")
    assert sommets4 == ['A', 'B', 'C']
    assert adj4 == {'A': ['B'], 'B': [], 'C': []}
    
    print("Tous les tests ont réussi!")

if __name__ == "__main__":
    test_charger_graphe()