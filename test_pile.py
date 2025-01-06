from outils import Pile

def test_pile():
    p = Pile()
    assert p.est_vide() == True, "La pile doit être vide à l'initialisation"
    
    p.empiler(1)
    p.empiler(2)
    assert p.est_vide() == False, "La pile ne doit pas être vide"
    assert p.sommet() == 2, "Le sommet devrait être 2"
    
    element = p.depiler()
    assert element == 2, "L'élément dépilé devrait être 2"
    assert p.sommet() == 1, "Le nouveau sommet devrait être 1"
    
    p.depiler()
    assert p.est_vide() == True, "La pile doit être vide après avoir tout dépilé"