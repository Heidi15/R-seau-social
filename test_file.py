from outils import File

def test_file():
    print("=== Test File ===")
    f = File()
    assert f.est_vide() == True, "La file devrait être vide à l'initialisation"
    
    f.enfiler(1)
    assert f.est_vide() == False, "La file ne devrait pas être vide après enfilement"
    
    f.enfiler(2)
    assert f.defiler() == 1, "Le premier élément défilé devrait être 1"
    assert f.defiler() == 2, "Le deuxième élément défilé devrait être 2"
    assert f.est_vide() == True, "La file devrait être vide après défilement"
    print("Tests File OK")

if __name__ == "__main__":
    test_file()
    print("\nTous les tests sont passés avec succès!")    