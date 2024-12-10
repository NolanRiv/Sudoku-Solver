class Accessors:
    """
    Classe permettant d'accéder aux cellules, lignes, colonnes et blocs
    d'une grille de Sudoku. Elle centralise les méthodes de type getter et setter.

    Méthodes : 
        get_cell : Récupère la valeur d'une cellule donnée.
        get_row : Récupère toute une ligne de la grille.
        get_column : Récupère toute une colonne de la grille.
        get_block : Récupère un bloc 3x3 de la grille.
        set_cell : Définit la valeur d'une cellule donnée.
    """

    @staticmethod
    def get_cell(grid, row_index, col_index) -> int:
        return grid[row_index][col_index]

    @staticmethod
    def get_row(grid, row_index) -> list[int]:
        return grid[row_index]

    @staticmethod
    def get_column(grid, col_index) -> list[int]:
        return [row[col_index] for row in grid]

    @staticmethod
    def get_block(grid, row_index, col_index) -> list[int]:
        block_row = row_index // 3 * 3
        block_col = col_index // 3 * 3
        return [
            grid[r][c]
            for r in range(block_row, block_row + 3)
            for c in range(block_col, block_col + 3)
        ]

    @staticmethod
    def set_cell(grid, row_index, col_index, value):
        grid[row_index][col_index] = value
