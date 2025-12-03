import math          # Import du module math (utilisé pour infini)
import itertools     # Import pour générer les permutations (brute force)


# --------------------------------------------------------------------
# Fonction à compléter : brute force TSP
# --------------------------------------------------------------------
def brute_force_tsp(distances):
    """
    distances : matrice NxN des distances entre les villes
    Retour attendu : (best_route, best_length)

    Les étudiants doivent :
    1. Fixer le point de départ (index 0 = Alger)
    2. Générer toutes les permutations des autres villes (1..n-1)
    3. Calculer la distance de chaque route
    4. Trouver la route minimale
    """

    

    return best_route, best_length         # retourner la meilleure solution trouvée



# --------------------------------------------------------------------
# Liste des 10 villes (leurs indices correspondent aux lignes/colonnes)
# --------------------------------------------------------------------
cities = [
    "Alger","Batna","Oran","Sétif","Constantine",
    "Tlemcen","Ouargla","Annaba","Béchar","Tizi-Ouzou"
]


# --------------------------------------------------------------------
# Matrice des distances entre les villes (symétrique)
# --------------------------------------------------------------------
D = [
    [0,   430, 415, 260, 320, 520, 770, 600, 970, 110],   # Alger
    [430,   0, 798, 100, 120, 620, 420, 300, 950, 350],   # Batna
    [415, 798,   0, 430, 500, 180, 850, 780, 720, 380],   # Oran
    [260, 100, 430,   0, 115, 500, 620, 310, 800, 250],   # Sétif
    [320, 120, 500, 115,   0, 550, 610, 160, 950, 340],   # Constantine
    [520, 620, 180, 500, 550,   0,1000, 720, 450, 540],   # Tlemcen
    [770, 420, 850, 620, 610,1000,   0, 720, 770, 640],   # Ouargla
    [600, 300, 780, 310, 160, 720, 720,   0,1150, 360],   # Annaba
    [970, 950, 720, 800, 950, 450, 770,1150,   0,1160],   # Béchar
    [110, 350, 380, 250, 340, 540, 640, 360,1160,   0]    # Tizi-Ouzou
]


# --------------------------------------------------------------------
# Appel de la fonction brute force
# --------------------------------------------------------------------
best_route, best_length = brute_force_tsp(D)


# --------------------------------------------------------------------
# Affichage du résultat
# --------------------------------------------------------------------
print("Best route :", best_route)      # les étudiants peuvent améliorer cet affichage
print("Best route length:", best_length)
