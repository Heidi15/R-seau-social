from outils import Pile

def test_pile():
    print("=== Test Pile ===")
    p = Pile()
    assert p.est_vide() == True, "La pile devrait être vide à l'initialisation"
    
    p.empiler(1)
    assert p.est_vide() == False, "La pile ne devrait pas être vide après empilement"
    
    p.empiler(2)
    assert p.depiler() == 2, "Le premier élément dépilé devrait être 2"
    assert p.depiler() == 1, "Le deuxième élément dépilé devrait être 1"
    assert p.est_vide() == True, "La pile devrait être vide après dépilement"
    print("Tests Pile OK")

if __name__ == "__main__":
    test_pile()
    print("\nTous les tests sont passés avec succès!")    