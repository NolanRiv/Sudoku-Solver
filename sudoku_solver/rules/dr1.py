from rules.deduction_rule import DeductionRule

class dr1(DeductionRule):
    """
    Première règle de déduction : "Naked Singles".
    Cette règle vérifie si une cellule n'a qu'une seule valeur candidate basée sur les nombres présents dans sa ligne, sa colonne et son bloc 3x3.

    Méthodes :
        apply() -> bool : Applique la règle de "Naked Singles". Si une cellule a un seul candidat, elle est remplie avec cette valeur et la grille est mise à jour.
    """

    def apply(self) -> bool:
        applied = False
        self.grid.update_candidates()

        for i in range(9):
            for j in range(9):
                candidates = self.grid.get_cell_candidates(i, j)
                if len(candidates) == 1:
                    answer = candidates.pop()
                    self.grid.set_cell(i, j, answer)
                    applied = True
        return applied