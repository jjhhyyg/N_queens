from PuzzleSolver import PuzzleSolver


if __name__ == '__main__':
    puzzle_solver = PuzzleSolver(8)
    puzzle_solver.solve(0)
    result = puzzle_solver.get_result()
    print(len(result))
    