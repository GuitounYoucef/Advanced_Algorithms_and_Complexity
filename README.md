# TP1 -- Manipulation de fichiers, dictionnaires et analyse de complexité

## 🎓 Objectif du TP

Ce travail pratique introduit les étudiants à : - La lecture et
l'écriture de fichiers en Python\
- La manipulation des listes et des dictionnaires\
- Le comptage des occurrences dans une liste\
- La mesure du temps d'exécution\
- L'analyse de la complexité temporelle (O(n²))

## 📁 Organisation du projet

    Practical_Work1/
    ├── dictionary_manipulation.py
    ├── files_handling.py
    ├── list_manipulation.py
    ├── main.py
    ├── numbers.txt
    ├── valeurs_aleatoires.txt
    └── README.md

## 🧪 Description du script principal

Le fichier **main.py** réalise les tâches suivantes : 1. Lecture du
fichier `valeurs_aleatoires.txt` et conversion en liste d'entiers. 2.
Comptage des occurrences à l'aide de deux boucles imbriquées (O(n²)). 3.
Affichage dynamique de la progression, du temps écoulé et du temps
restant. 4. Affichage final : durée d'exécution, nombre d'itérations,
complexité.

## 🧠 Notions abordées

-   Manipulation de fichiers (`open`, lecture ligne par ligne)
-   Structures Python : listes et dictionnaires
-   Analyse de performance et estimation du temps
-   Affichage temps réel avec `sys.stdout.write()` et `flush()`

## 🚀 Exécution

Dans un terminal :

    python main.py

## ❗ Problèmes possibles

-   **KeyboardInterrupt** : interruption manuelle du script (Ctrl+C).
-   **File not found** : évité grâce à
    `os.chdir(os.path.dirname(__file__))`.

## 📌 À retenir

Ce TP démontre l'impact d'un algorithme en O(n²) sur de grandes données
et l'importance des structures de données adaptées pour optimiser la
complexité.

## Cloner le dépôt GitHub

Pour cloner ce dépôt sur votre machine, exécutez la commande suivante dans votre terminal :

```bash
git clone https://github.com/GuitounYoucef/Advanced_Algorithms_and_Complexity.git
```

Ensuite, entrez dans le dossier cloné :

```bash
cd Advanced_Algorithms_and_Complexity
```

Puis lancez votre code comme indiqué dans les instructions précédentes.

