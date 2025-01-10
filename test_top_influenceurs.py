from outils import top_influenceurs

def test_top_influenceurs():
    print("=== Test top influenceurs ===")
    sommets = ['A', 'B', 'C']
    matrice = [
        [0, 0, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]
    influenceurs = top_influenceurs(sommets, matrice)
    assert 'A' in influenceurs, "A devrait être un top influenceur"
    assert len(influenceurs) == 1, "Il devrait y avoir un seul top influenceur"
    print("Tests top influenceurs OK")

if __name__ == "__main__":
    test_top_influenceurs()
    print("\nTous les tests sont passés avec succès!")    