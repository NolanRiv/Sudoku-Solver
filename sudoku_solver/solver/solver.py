from rules.dr1 import dr1
from rules.dr2 import dr2
from rules.dr3 import dr3
from grid.grid import SudokuGrid
from solver.difficulty_solver import Difficulty

class SudokuSolver:
    """
    Résout une grille de Sudoku en appliquant des règles de déduction et des niveaux de difficulté.

    Arguments :
        grid_file (str) : Le chemin vers le fichier contenant la grille de Sudoku (format CSV).

    Méthodes :
        __init__(grid_file: str) : Initialise l'objet avec la grille de Sudoku à partir d'un fichier.
        show_grid() : Affiche la grille actuelle de Sudoku.
        is_solved() -> bool : Vérifie si la grille est valide et complète.
        solve() -> None : Résout la grille en appliquant les règles et niveaux de difficulté.
    """

    def __init__(self, grid_file: str):
        with open(grid_file, 'r') as file:
            self.grid = SudokuGrid([list(map(int, line.split(','))) for line in file])
        self.dr1 = dr1(self.grid)
        self.dr2 = dr2(self.grid)
        self.dr3 = dr3(self.grid)
        self.difficulty = Difficulty(self)

    def show_grid(self):
        """
        Affiche la grille actuelle de Sudoku.
        """
        print(self.grid)

    def is_solved(self) -> bool:
        """
        Vérifie si la grille est valide et complète.

        :return: True si la grille est valide et complète, False sinon.
        """
        return self.grid.is_valid() and self.grid.is_complete()

    def solve(self) -> None:
        """
        Résout la grille en appliquant les règles de déduction et les niveaux de difficulté.

        :return: None
        """
        self.show_grid()

        if self.difficulty.easy():
            return
        if self.difficulty.medium():
            return
        self.difficulty.hard()