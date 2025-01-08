from outils import matrice, liste

def test_aretes():

    matriceadj= [[0,1,1],
                 [1,0,1],
                 [1,1,0]]

    matriceobj= matrice(matriceadj)
    assert matriceobj.aretesmatrice() == 3, "La matrice doit avoir 3 arêtes"

    listeadj = [[1, 0], 
                [2, 1],  
                [1, 3],  
                [0, 2]]

    listeobj = liste(listeadj)
    assert listeobj.aretesliste() == 4, "La liste doit avoir 4 arêtes"

if __name__ == "__main__":
    test_aretes()
    print("Tests des aretes réussis!")

