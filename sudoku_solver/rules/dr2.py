from collections import Counter
import functools
from rules.deduction_rule import DeductionRule

class dr2(DeductionRule):
    """
    Deuxième règle de déduction : "Hidden Singles".
    Cette règle vérifie, pour un nombre donné, si une cellule est la seule dans sa ligne, colonne ou bloc 3x3 à avoir ce nombre comme candidat.

    Méthodes :
        apply() -> bool : Applique la règle des "Hidden Singles" sur toute la grille.
        _apply_to_group(candidates_func, group_index) -> bool : Applique la règle à une ligne, colonne ou bloc spécifique.
    """

    def apply(self) -> bool:
        applied = False
        self.grid.update_candidates()

        for group_index in range(9):
            applied = applied or self._apply_to_group(super()._get_row_candidates, group_index, 'row')
            applied = applied or self._apply_to_group(super()._get_col_candidates, group_index, 'column')
            applied = applied or self._apply_to_group(super()._get_block_candidates, group_index, 'block')

        return applied

    def _apply_to_group(self, candidates_func, group_index, group_type) -> bool:
        applied = False
        candidates = candidates_func(self.grid, group_index)
        if candidates:
            candidates = Counter(functools.reduce(lambda x, y: x + y, candidates))
            for candidate, count in candidates.items():
                if count == 1:
                    for element_index in range(9):
                        row_index, col_index = super()._get_indices(candidates_func, group_index, element_index)
                        if candidate in self.grid.get_cell_candidates(row_index, col_index):
                            self.grid.set_cell(row_index, col_index, candidate)
                            self.grid.update_candidates()
                            applied = True
        return applied