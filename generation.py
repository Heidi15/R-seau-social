import random
import argparse

class Generation:
    def __init__(self):
        self.graphe = {}

    def creation(self, oriente, total, min_deg, max_deg, communaute):
        self.graphe = {i: [] for i in range(total)}
        
        communautes = []
        for i in range(communaute):
            start = i * (total // communaute)
            end = (i + 1) * (total // communaute) if i != communaute - 1 else total
            communautes.append(list(range(start, end)))

        for i in range(total):
       
            while len(self.graphe[i]) < min_deg:
                cible = random.choice(communautes[i // (total // communaute)])
                if cible != i and cible not in self.graphe[i]:
                    self.graphe[i].append(cible)
                    if not oriente:  
                        self.graphe[cible].append(i)

            while len(self.graphe[i]) < max_deg:
                cible = random.choice(communautes[i // (total // communaute)])
                if cible != i and cible not in self.graphe[i]:
                    self.graphe[i].append(cible)
                    if not oriente: 
                        self.graphe[cible].append(i)

    def enregistrer_graphe(self, fichier):
        with open(fichier, "w") as f:
            for sommet in range(len(self.graphe)):
                voisins = " ".join(map(str, self.graphe[sommet]))
                f.write(f"{sommet}: {voisins}\n")

def main():
    parser = argparse.ArgumentParser(description="Générer un graphe aléatoire avec contraintes.")
    parser.add_argument("--sommets", type=int, required=True, help="Nombre de sommets dans le graphe")
    parser.add_argument("--degre_min", type=int, required=True, help="Degré minimum des sommets")
    parser.add_argument("--degre_max", type=int, required=True, help="Degré maximum des sommets")
    parser.add_argument("--oriente", type=bool, default=False, help="Si le graphe est orienté (True/False)")
    parser.add_argument("--communaute", type=int, required=True, help="Nombre de communautés")
    parser.add_argument("--fichier", type=str, required=True, help="Nom du fichier pour sauvegarder le graphe")

    args = parser.parse_args()

    generateur = Generation()
    generateur.creation(args.oriente, args.sommets, args.degre_min, args.degre_max, args.communaute)
    generateur.enregistrer_graphe(args.fichier)

    print(f"Graphe généré et sauvegardé dans le fichier {args.fichier}")

if __name__ == "__main__":
    main()
