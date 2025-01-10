from outils import parcours_profondeur, parcours_largeur

def test_parcours():
    print("=== Test parcours ===")
    # Créer un petit graphe de test
    sommets = ['A', 'B', 'C', 'D']
    matrice = [
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 1, 0]
    ]
    
    # Test parcours en profondeur
    visites_prof = parcours_profondeur(sommets, matrice, 'A')
    assert len(visites_prof) == 4, "Le parcours devrait visiter tous les sommets"
    assert visites_prof[0] == 'A', "Le parcours devrait commencer par A"
    
    # Test parcours en largeur
    visites_larg = parcours_largeur(sommets, matrice, 'A')
    assert len(visites_larg) == 4, "Le parcours devrait visiter tous les sommets"
    assert visites_larg[0] == 'A', "Le parcours devrait commencer par A"
    print("Tests parcours OK")

if __name__ == "__main__":
    test_parcours()
    print("\nTous les tests sont passés avec succès!")    