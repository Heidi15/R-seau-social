from outils import File

def test_file():
    f = File()
    assert f.est_vide() == True, "La file doit être vide à l'initialisation"
    
    f.enfiler(1)
    f.enfiler(2)
    assert f.est_vide() == False, "La file ne doit pas être vide"
    assert f.premier() == 1, "Le premier élément devrait être 1"
    
    element = f.defiler()
    assert element == 1, "L'élément défilé devrait être 1"
    assert f.premier() == 2, "Le nouveau premier élément devrait être 2"
    
    f.defiler()
    assert f.est_vide() == True, "La file doit être vide après avoir tout défilé"

if __name__ == "__main__":
    test_file()
    print("Tests de la file réussis!")