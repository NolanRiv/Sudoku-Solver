import os
from solver.solver import SudokuSolver

def main():
    puzzle_file = "utils/sudoku.txt"
    if not os.path.exists(puzzle_file):
        print(f"Error: Le fichier {puzzle_file} n'existe pas.")
        return

    solver = SudokuSolver(puzzle_file)

    try:
        solver.solve()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()