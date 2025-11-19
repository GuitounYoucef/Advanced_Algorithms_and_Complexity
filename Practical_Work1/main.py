import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

#############################################################################################################################

def read_file(file_name):
    # Ouvre le fichier en mode lecture 'r'
    file = open(file_name, 'r')
    values = []   # Liste qui va contenir les entiers du fichier
    for line in file:
        # Convertir chaque ligne en entier et l'ajouter à la liste
        values.append(int(line.strip()))
    file.close()  # Fermer le fichier après lecture
    return values    

#############################################################################################################################

# Debut du script principal
value_list = read_file('valeurs_aleatoires.txt')

print(value_list)
list_length = len(value_list)
n = len(value_list)
print('Longueur de la liste :', n)

iterations = 0
start_time = time.time()
occurrences = dict()
remaining_time = 0

for i in range(n):
    iterations += 1
    count = 0
    for j in range(n):
        iterations += 1
        if value_list[j] == value_list[i]:
            count += 1
        occurrences[value_list[i]] = count
    

    #               100% --> n
    # elapsed_percentage --> i+1 => elapsed_percentage  = (i + 1) * 100 / n  
    elapsed_percentage   = (i + 1) * 100 / n
    remaining_percentage = 100 - elapsed_percentage 

    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_percentage  > 0:
        #    elapsed_time --> elapsed_percentage 
        #  remaining_time --> remaining_percentage => remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
        remaining_time = remaining_percentage * elapsed_time / elapsed_percentage 
    
    # Affiche la progression sur une seule ligne en écrasant l'affichage précédent.
    # \r ramène le curseur au début de la ligne, sys.stdout.write écrit le texte sans retour à la ligne,
    # et le formatage affiche le pourcentage, le temps écoulé et le temps restant estimé.
    sys.stdout.write(f"\rProgress: {elapsed_percentage :.2f}%, Elapsed Time: {elapsed_time:.2f}s, RemainingTime: {remaining_time:.2f}s")

    # Force l'affichage immédiat du texte (sinon Python peut attendre avant d'afficher).
    sys.stdout.flush()  

end_time = time.time()
print(f"\n⏱ Durée totale du comptage : {end_time - start_time:.5f} secondes")
print(f"Nombre total d’itérations : {iterations}")




