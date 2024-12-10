class Validator:
    """
    Classe pour valider une grille de Sudoku.

    Méthodes :
        is_complete() -> bool : Vérifie si la grille est complète (aucune cellule avec la valeur 0).
        is_valid() -> bool : Vérifie si la grille respecte les règles de Sudoku (valeurs uniques dans chaque ligne, colonne et bloc).
        _is_valid_group(group) -> bool : Vérifie si un groupe de cellules (ligne, colonne ou bloc) est valide.
    """

    def __init__(self, grid):
        self.grid = grid

    @staticmethod
    def _is_valid_group(group):
        seen = set()
        for num in group:
            if num != 0:
                if num in seen or num < 1 or num > 9:
                    return False
                seen.add(num)
        return True

    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.grid.get_cell(i, j) == 0:
                    return False
        return True

    def is_valid(self):
        for i in range(9):
            row = self.grid.get_row(i)
            col = self.grid.get_column(i)
            block = self.grid.get_block((i // 3) * 3, (i % 3) * 3)
            if not self._is_valid_group(row) or not self._is_valid_group(col) or not self._is_valid_group(block):
                return False
        return True