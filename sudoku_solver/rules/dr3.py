from rules.deduction_rule import DeductionRule

class dr3(DeductionRule):
    """
    Troisième règle de déduction : "Naked Pairs".
    Cette règle recherche des paires de cellules dans une même ligne, colonne ou bloc qui ont les mêmes deux candidats.
    Si une paire est trouvée, ces deux candidats sont supprimés des autres cellules de cette ligne, colonne ou bloc.

    Méthodes :
        apply() -> bool : Applique la règle des "Naked Pairs" sur toute la grille.
        _apply_to_group(candidates_func, group_index: int) -> bool : Applique la règle à une ligne, colonne ou bloc donné.
    """

    def apply(self) -> bool:
        applied = False
        for group_index in range(9):
            applied = applied or self._apply_to_group(super()._get_row_candidates, group_index, "row")
            applied = applied or self._apply_to_group(super()._get_col_candidates, group_index, "column")
            applied = applied or self._apply_to_group(super()._get_block_candidates, group_index, "block")
        return applied

    def _apply_to_group(self, candidates_func, group_index: int, group_type: str) -> bool:
        applied = False
        candidates = candidates_func(self.grid, group_index)

        if candidates:
            pairs = [tuple(sorted(pair)) for pair in candidates if len(pair) == 2]
            if len(pairs) != len(set(pairs)):
                duplicates = [list(x) for n, x in enumerate(pairs) if x in pairs[:n]]
                for pair in duplicates:
                    for element_index in range(9):
                        row_index, col_index = super()._get_indices(candidates_func, group_index, element_index)
                        if self.grid.get_cell_candidates(row_index, col_index) != pair:
                            for candidate in pair:
                                if candidate in self.grid.get_cell_candidates(row_index, col_index):
                                    self.grid.get_cell_candidates(row_index, col_index).remove(candidate)
                                    applied = True
                                    self.grid.update_candidates()
        return applied