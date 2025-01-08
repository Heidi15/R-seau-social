# Fonction pour déterminer si le réseau social est une seule communauté
def est_une_seule_communauté(matrice_adjacence):
    
    def dfs(sommet, visites):
        """Effectue un parcours en profondeur à partir d'un sommet donné."""
        visites[sommet] = True
        for voisin, est_adjacent in enumerate(matrice_adjacence[sommet]):
            if est_adjacent == 1 and not visites[voisin]:
                dfs(voisin, visites)

    
    n = len(matrice_adjacence)

    visites = [False] * n

    dfs(0, visites)

    return all(visites)

def test_est_une_seule_communauté():
    
    matrice1 = [
        [0, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0]
    ]
    assert est_une_seule_communauté(matrice1) == True

    matrice2 = [
        [0, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ]
    assert est_une_seule_communauté(matrice2) == False

    print("Tests réussies !")

if __name__ == "__main__":
    test_est_une_seule_communauté()
