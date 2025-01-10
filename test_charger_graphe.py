from outils import charger_graphe, nombre_arcs_matrice, nombre_arcs_liste

def test_charger_graphe():
    print("=== Test chargement de graphe ===")
    # Test avec le fichier go-9-01.txt
    sommets, matrice = charger_graphe("go-9-01.txt", "matrice")
    assert len(sommets) == 9, "Le graphe devrait avoir 9 sommets"
    assert nombre_arcs_matrice(matrice) == 21, "Le graphe devrait avoir 21 arcs"
    
    sommets, liste = charger_graphe("go-9-01.txt", "liste")
    assert len(sommets) == 9, "Le graphe devrait avoir 9 sommets"
    assert nombre_arcs_liste(liste) == 21, "Le graphe devrait avoir 21 arcs"
    print("Tests chargement de graphe OK")

if __name__ == "__main__":
    test_charger_graphe()
    print("\nTous les tests sont passés avec succès!")    