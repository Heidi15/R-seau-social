from outils import chemin_minimum

def test_chemin_minimum():
    # Définition d'un réseau de test
    reseau = {
        "Alice": ["Bob", "Carol"],
        "Bob": ["Diane"],
        "Carol": ["Eve", "Diane"],
        "Diane": ["Eve"],
        "Eve": []
    }

    # Test 1: Chemin direct
    resultat = chemin_minimum(reseau, "Alice", "Bob")
    assert resultat == ["Alice", "Bob"], f"Test chemin direct échoué: {resultat}"

    # Test 2: Chemin avec intermédiaire
    resultat = chemin_minimum(reseau, "Alice", "Diane")
    assert len(resultat) == 3, f"Test longueur chemin échoué: {resultat}"
    assert resultat[0] == "Alice", f"Test début chemin échoué: {resultat}"
    assert resultat[-1] == "Diane", f"Test fin chemin échoué: {resultat}"

    # Test 3: Chemin inexistant
    resultat = chemin_minimum(reseau, "Eve", "Alice")
    assert resultat == [], f"Test chemin inexistant échoué: {resultat}"

    # Test 4: Source inexistante
    resultat = chemin_minimum(reseau, "Frank", "Alice")
    assert resultat == [], f"Test source inexistante échoué: {resultat}"

    # Test 5: Réseau vide
    resultat = chemin_minimum({}, "Alice", "Bob")
    assert resultat == [], f"Test réseau vide échoué: {resultat}"

    print("Tous les tests ont réussi!")

if __name__ == "__main__":
    from collections import deque
    
    def chemin_minimum(reseau, source, cible):
        file = deque([(source, [source])])
        visites = set()
        
        while file:
            personne_actuelle, chemin_actuel = file.popleft()
            
            if personne_actuelle == cible:
                return chemin_actuel
            
            visites.add(personne_actuelle)
            
            for voisin in reseau.get(personne_actuelle, []):
                if voisin not in visites:
                    file.append((voisin, chemin_actuel + [voisin]))
        
        return []

    test_chemin_minimum()