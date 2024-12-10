from grid.accessors import Accessors
from grid.candidate_manager import CandidateManager
from grid.validator import Validator

class SudokuGrid:
    """
    Représentation d'une grille de Sudoku sous forme de matrice 9x9.
    Une seule instance de cette classe existe à tout moment (Singleton).

    Méthodes :
        __new__ : Crée une nouvelle instance si elle n'existe pas.
        __init__ : Initialise la grille de Sudoku avec les valeurs données.
        __repr__ : Retourne une représentation textuelle de la grille.
        is_complete : Vérifie si la grille est complète (aucune cellule vide).
        is_valid : Vérifie si la grille est valide selon les règles du Sudoku.
    """
    instance = None

    def __new__(cls, *args):
        if not cls.instance:
            cls.instance = super(SudokuGrid, cls).__new__(cls)
        return cls.instance

    def __init__(self, grid):
        if not hasattr(self, 'grid'):
            self.grid = grid
            self.candidates = {(i, j): list() for i in range(9) for j in range(9)}
            self.candidate_manager = CandidateManager(self)
            self.validator = Validator(self)

    def __repr__(self):
        r = ""
        for i in range(9):
            for j in range(9):
                r += str(self.grid[i][j]) if self.grid[i][j] else '.'
                if j != 8:
                    r += ' '
                if (j + 1) % 3 == 0 and j != 8:
                    r += ('|' + ' ')
            r += '\n'
            if (i + 1) % 3 == 0 and i != 8:
                r += '––––––|–––––––|––––––\n'
        return r

    def get_cell(self, row_index, col_index) -> int:
        return Accessors.get_cell(self.grid, row_index, col_index)

    def get_row(self, row_index) -> list[int]:
        return Accessors.get_row(self.grid, row_index)

    def get_column(self, col_index) -> list[int]:
        return Accessors.get_column(self.grid, col_index)

    def get_block(self, row_index, col_index) -> list[int]:
        return Accessors.get_block(self.grid, row_index, col_index)

    def set_cell(self, row_index, col_index, value):
        Accessors.set_cell(self.grid, row_index, col_index, value)

    def update_candidates(self):
        self.candidate_manager.update_candidates()

    def get_cell_candidates(self, row_index, col_index) -> list[int]:
        return self.candidates[(row_index, col_index)]

    def is_complete(self):
        return self.validator.is_complete()

    def is_valid(self):
        return self.validator.is_valid()
