from outils import temps_propagation, chemin_propagation

def test_propagation():
    print("=== Test propagation ===")
    sommets = ['A', 'B', 'C', 'D']
    matrice = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    
    # Test temps de propagation
    temps = temps_propagation(sommets, matrice, 'A', 'D')
    assert temps == 15, "La propagation devrait prendre 15 minutes (3 sauts * 5 minutes)"
    
    # Test chemin de propagation
    chemin = chemin_propagation(sommets, matrice, 'A', 'D')
    assert chemin == ['A', 'B', 'C', 'D'], "Le chemin devrait être A->B->C->D"
    print("Tests propagation OK")

if __name__ == "__main__":
    test_propagation()
    print("\nTous les tests sont passés avec succès!")