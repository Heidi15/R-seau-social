from outils import Aretes

def test_aretes():
    matrice = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    a_matrice = Aretes(matrice)
    assert a_matrice.aretesmatrice() == 2

    liste = [[0, 1], [1, 2], [2, 0]]
    a_liste = Aretes(liste)
    assert a_liste.aretesliste() == 3

if __name__ == '__main__':
    test_aretes()
    print("Tous les tests ont réussi.")