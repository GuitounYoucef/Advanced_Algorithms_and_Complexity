import time
import sys
import os

# Changer le répertoire courant vers celui où se trouve le script. 
# Cela évite les erreurs "file not found" lorsque vous lisez ou écrivez des fichiers.
os.chdir(os.path.dirname(__file__))

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
file = open('valeurs_aleatoires.txt','r')
f= file.readlines()

valeurs_list=read_file('valeurs_aleatoires.txt')


print(valeurs_list)
list_length = len(valeurs_list)
n = len(valeurs_list)
print('list Length : ',n)

iterations = 0
start = time.time()
occurrences = dict()
RemainingTime = 0 
for i in range(n):
    iterations += 1
    count = 0
    for j in range(n):
        iterations += 1
        if valeurs_list[j] == valeurs_list[i]:
            count += 1
        occurrences[valeurs_list[i]] = count
    percentage = (i + 1) * 100 / n
    RemainingP=100 - percentage
    current = time.time()
    Elapsed = current - start
    if percentage > 0: 
       RemainingTime = RemainingP * Elapsed / percentage 
    
    sys.stdout.write(f"\rProgress: {percentage:.2f}%, Elapsed Time: {current - start:.2f}s, RemainingTime Time: {RemainingTime/3600:.2f}H",  )
    sys.stdout.flush()     

end = time.time()
print(f"⏱ Durée du comptage : {end - start:.5f} secondes")
print(f"🔁 Nombre total d’itérations : {iterations}")
print("Complexité : O(n²)\n")



