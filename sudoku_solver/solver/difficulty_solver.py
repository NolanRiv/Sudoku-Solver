class Difficulty:
    """
    Gère la résolution du Sudoku en fonction de la difficulté : Facile, Moyenne, Difficile.

    Méthodes :
        __init__(self, solver) -> None : Initialise l'objet Difficulty avec un solver.
        easy(self) -> bool : Applique la règle DR1 pour résoudre un Sudoku facile.
        medium(self) -> bool : Applique la règle DR2 pour résoudre un Sudoku moyen.
        hard(self) -> None : Applique les règles DR3, DR2, DR1 pour résoudre un Sudoku difficile.
        ask_user_for_input(self) -> None : Demande à l'utilisateur d'entrer une cellule lorsque toutes les règles échouent.
    """
    def __init__(self, solver):
        self.solver = solver

    def easy(self) -> bool:
        while self.solver.dr1.apply():
            pass
        if self.solver.is_solved():
            self.solver.show_grid()
            print("Difficulté: Facile")
            return True
        return False

    def medium(self) -> bool:
        while self.solver.dr2.apply():
            pass
        if self.solver.is_solved():
            self.solver.show_grid()
            print("Difficulté: Moyenne")
            return True
        return False

    def hard(self) -> None:
        input_required = False
        rules = [self.solver.dr3, self.solver.dr2, self.solver.dr1]
        
        while not self.solver.is_solved():
            applied = False
            # Applique les règles DR3, DR2, DR1 à chaque itération
            for rule in rules:
                applied = applied or rule.apply()
            
            if not applied:
                # Si aucune règle n'a pu être appliquée, demande à l'utilisateur de remplir une cellule
                self.solver.show_grid()
                self.ask_user_for_input()
                input_required = True
                if not self.solver.grid.is_valid():
                    print("Erreur : Veuillez recommencer depuis le début.")
                    return

            # Une fois l'entrée utilisateur effectuée, on redémarre le processus de test des règles
            print("Application des règles après l'entrée utilisateur...")
            while self.solver.dr1.apply() or self.solver.dr2.apply() or self.solver.dr3.apply():
                pass

        self.solver.show_grid()
        print(f"Difficulté: {'Très Difficile' if input_required else 'Difficile'}")

    def ask_user_for_input(self) -> None:
        print("Toutes les règles de déduction ont échoué, entrez une solution.")

        while True:
            try:
                row, col, val = input("Format demandé (ex: 0 (ligne), 1 (colonne), 5 (valeur)) = 0,1,5 (l'index commence à 0): ").split(',')
                row, col, val = int(row), int(col), int(val)

                # Vérification que les indices sont dans les limites de la grille (0-8)
                if not (0 <= row < 9 and 0 <= col < 9):
                    print("Erreur: les indices de ligne et colonne doivent être compris entre 0 et 8.")
                    continue

                # Vérification que la valeur est valide (entre 1 et 9)
                if not (1 <= val <= 9):
                    print("Erreur: la valeur doit être comprise entre 1 et 9.")
                    continue

                # Vérification que la cellule n'est pas déjà remplie
                if self.solver.grid.get_cell(row, col) != 0:
                    print(f"Erreur: la cellule ({row},{col}) est déjà remplie avec la valeur {self.solver.grid.get_cell(row, col)}.")
                    continue

                # Si toutes les conditions sont remplies, on applique la valeur
                self.solver.grid.set_cell(row, col, val)
                print(f"Cellule ({row},{col}) mise à jour avec la valeur {val}.")
                break
            except ValueError:
                print("Erreur: format d'entrée invalide. Assurez-vous de saisir trois valeurs séparées par des virgules.")