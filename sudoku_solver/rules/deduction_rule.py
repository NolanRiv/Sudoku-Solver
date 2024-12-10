from abc import ABC, abstractmethod
from grid.grid import SudokuGrid

class DeductionRule(ABC):
    """
    Classe abstraite pour les règles de déduction du Sudoku.

    Arguments :
        grid (SudokuGrid) : La grille de Sudoku sur laquelle la règle de déduction sera appliquée.

    Méthodes :
        __init__(grid: SudokuGrid) : Initialise la règle de déduction avec la grille de Sudoku.
        apply() -> bool : Applique la règle de déduction à la grille. Retourne True si la grille a été modifiée, False sinon.
        _get_row_candidates : Récupère les candidats pour une ligne donnée.
        _get_col_candidates : Récupère les candidats pour une colonne donnée.
        _get_block_candidates : Récupère les candidats pour un bloc donné.
        _get_indices : Détermine les indices appropriés en fonction de la fonction de candidats.
    """

    def __init__(self, grid: SudokuGrid):
        self.grid = grid

    @abstractmethod
    def apply(self) -> bool:
        raise NotImplementedError

    @classmethod
    def _get_row_candidates(cls, grid: SudokuGrid, row_index: int) -> list[list[int]]:
        return [grid.get_cell_candidates(row_index, j) for j in range(9) if grid.get_cell_candidates(row_index, j)]

    @classmethod
    def _get_col_candidates(cls, grid: SudokuGrid, col_index: int) -> list[list[int]]:
        return [grid.get_cell_candidates(j, col_index) for j in range(9) if grid.get_cell_candidates(j, col_index)]

    @classmethod
    def _get_block_candidates(cls, grid: SudokuGrid, block_index: int) -> list[list[int]]:
        return [grid.get_cell_candidates((block_index // 3) * 3 + (j // 3), (block_index % 3) * 3 + (j % 3)) for j
                in range(9) if
                grid.get_cell_candidates((block_index // 3) * 3 + (j // 3), (block_index % 3) * 3 + (j % 3))]

    @classmethod
    def _get_indices(cls, candidates_func, i, j):
        if candidates_func == cls._get_row_candidates:
            return i, j
        if candidates_func == cls._get_col_candidates:
            return j, i
        if candidates_func == cls._get_block_candidates:
            return (i // 3) * 3 + (j // 3), (i % 3) * 3 + (j % 3)