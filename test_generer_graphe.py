from outils import generer_graphe

def test_generation_graphe():
    print("=== Test génération de graphe ===")
    
    # Test 1: Graphe orienté simple
    print("Test 1: Graphe orienté simple")
    sommets, matrice = generer_graphe(5, est_oriente=True, degre_min=1, degre_max=3)
    assert len(sommets) == 5, "Le graphe devrait avoir 5 sommets"
    for i in range(5):
        degre = sum(matrice[i])
        assert degre >= 1 and degre <= 3, f"Le degré du sommet {i} ({degre}) devrait être entre 1 et 3"
    
    # Test 2: Graphe non orienté
    print("Test 2: Graphe non orienté")
    sommets, matrice = generer_graphe(4, est_oriente=False, degre_min=2, degre_max=3)
    assert len(sommets) == 4, "Le graphe devrait avoir 4 sommets"
    for i in range(4):
        for j in range(4):
            assert matrice[i][j] == matrice[j][i], "La matrice devrait être symétrique"
    
    # Test 3: Graphe avec communautés
    print("Test 3: Graphe avec communautés")
    sommets, matrice = generer_graphe(6, nb_communautes=2)
    assert len(sommets) == 6, "Le graphe devrait avoir 6 sommets"
    # Vérifie que les communautés sont connectées
    assert any(matrice[i][j] == 1 for i in range(3) for j in range(3, 6)), \
           "Les communautés devraient être connectées"
    
    # Test 4: Graphe avec distance maximale
    print("Test 4: Graphe avec distance maximale")
    sommets, matrice = generer_graphe(4, distance_max=2)
    # Vérifie la distance maximale avec un parcours en largeur
    for depart in range(4):
        distances = [-1] * 4
        distances[depart] = 0
        file = [(depart, 0)]
        while file:
            sommet, dist = file.pop(0)
            for voisin in range(4):
                if matrice[sommet][voisin] == 1 and distances[voisin] == -1:
                    assert dist + 1 <= 2, "La distance maximale devrait être respectée"
                    distances[voisin] = dist + 1
                    file.append((voisin, dist + 1))
    
    # Test 5: Vérification du fichier généré
    print("Test 5: Vérification du fichier généré")
    filename = "test_graphe.txt"
    sommets, matrice = generer_graphe(3, filename=filename)
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert "GRAPHE ORIENTE" in lines[0], "Le fichier devrait indiquer un graphe orienté"
        assert "3 SOMMETS" in lines[1], "Le fichier devrait indiquer 3 sommets"
    
    print("Tests génération de graphe OK")

if __name__ == "__main__":
    test_generation_graphe()
    print("\nTous les tests sont passés avec succès!")