class CandidateManager:
    """
    Gère les candidats possibles pour chaque cellule de la grille de Sudoku.

    Méthodes :
        __init__ : Initialise le gestionnaire de candidats pour une grille donnée.
        update_candidates : Met à jour les candidats possibles pour chaque cellule.
    """
    def __init__(self, grid):
        self.grid = grid

    def update_candidates(self):
        numbers = set(range(1, 10))
        for i in range(9):
            for j in range(9):
                if self.grid.get_cell(i, j) == 0:
                    row = self.grid.get_row(i)
                    col = self.grid.get_column(j)
                    block = self.grid.get_block(i, j)
                    previous_candidates = self.grid.get_cell_candidates(i, j)

                    cell_candidates = numbers - set(row) - set(col) - set(block)
                    if previous_candidates:
                        cell_candidates = cell_candidates.intersection(set(previous_candidates))
                    self.grid.candidates[(i, j)] = sorted(list(cell_candidates))
                else:
                    self.grid.candidates[(i, j)] = list()