**Sudoku Solver**

Ce projet implémente un **solveur de Sudoku** en Python. Il est conçu pour résoudre des puzzles de Sudoku à partir d'une grille linéarisée, tout en appliquant des règles de déduction (DR1, DR2, DR3) pour trouver la solution.

---

### Structure du projet

`Sudoku Solver/

│

├── Docs/ # Documentation du projet

├── sudoku_solver/ # Code source de l'application

│ ├── grid/ # Classes et méthodes liées à la grille de Sudoku

│ ├── solver/ # Logique de résolution du puzzle

│ ├── rules/ # Implémentation des règles de déduction (DR1, DR2, DR3)

│ ├── main.py # Point d'entrée de l'application

│ └── sudoku.txt # Grille de Sudoku d'entrée

│

└── utils/ # Contient la grille de sudoku à remplir`

---

### Utilisation

#### 1\. Modifier le fichier de puzzle (`sudoku.txt`)

Le fichier `sudoku.txt` contient la grille du Sudoku que vous souhaitez résoudre. Chaque ligne de la grille doit être une séquence de chiffres (0 pour une case vide), et chaque fichier doit contenir exactement 81 caractères (9x9).

**Exemple de grille dans `sudoku.txt` :**

`5 3 0 0 7 0 0 0 0

6 0 0 1 9 5 0 0 0

0 9 8 0 0 0 0 6 0

8 0 0 0 6 0 0 0 3

4 0 0 8 0 3 0 0 1

7 0 0 0 2 0 0 0 6

0 6 0 0 0 0 2 8 0

0 0 0 4 1 9 0 0 5

0 0 0 0 8 0 0 7 9`

---

#### 2\. Exécution du programme

Une fois la grille prête, lancez le programme avec la commande suivante :

`python sudoku_solver/main.py`

---

#### 3\. Résolution du puzzle

Le programme lira automatiquement la grille de Sudoku à partir du fichier `sudoku.txt`, puis résoudra le puzzle en utilisant les règles de déduction. Le résultat sera affiché dans la console avec la grille complète.

---

#### 4\. Interaction avec l'utilisateur

Le programme peut demander à l'utilisateur de spécifier un mouvement à effectuer dans la grille. Par exemple, l'utilisateur peut entrer un chiffre pour remplir une case vide.

**Exemple d'interaction possible :**

**Grille initiale :**

`. 9 3 | 4 . . | . 6 .

8 6 . | . . . | . . 2

5 . . | . 8 . | . 9 7

------------|--------------|------------

7 . 9 | . . . | 6 8 5

6 1 . | . . 8 | . 3 4

. . . | . . 4 | . . .

------------|--------------|------------

. . 5 | 8 . 1 | . . .

. . . | 3 . . | . . .

9 8 . | 2 5 . | . . .`

**Message du programme :**\
"**Toutes les règles de déduction ont échoué, entrez une solution.**\
Format demandé (ex: 0 (ligne), 1 (colonne), 5 (valeur)) = 0,1,5 (l'index commence à 0) :"

L'utilisateur peut entrer une solution sous le format `ligne,colonne,valeur`. Exemple : `0,1,5`.

---

#### 5\. Résolution automatique

Le programme applique les règles de déduction suivantes pour résoudre le puzzle automatiquement :

- **DR1 :** Recherche de chiffres uniques dans une ligne, une colonne ou une région.
- **DR2 :** Déduction par élimination, lorsque la seule option restante est évidente.
- **DR3 :** Techniques avancées de déduction pour optimiser la recherche de solutions.

Une fois ces règles appliquées, le programme résout automatiquement le puzzle et affiche la solution.

---

### Fonctionnalités

- **Lecture de puzzle Sudoku :** Le programme lit une grille de Sudoku à partir du fichier `sudoku.txt`, où les cases vides sont représentées par `0`.

- **Application des règles de déduction :**\
  Trois règles de déduction sont appliquées pour résoudre le puzzle :

  - **DR1 :** Recherche de chiffres uniques dans une ligne, une colonne ou une région.
  - **DR2 :** Déduction par élimination, lorsque la seule option restante est évidente.
  - **DR3 :** Techniques avancées de déduction pour optimiser la recherche de solutions.

- **Résolution automatique :** Après l'application des règles, le programme résout automatiquement le puzzle et affiche la grille complète résolue.

---

### Important

- **Grille actuelle :** La Grille actuelle nécessitera forcément une action humaine. Pour faire avancer la grille et relancer le calcul denouveau, 2 coups doivent être rentrer : 4,2,9 puis 3,1,4.
