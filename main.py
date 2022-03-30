from PuzzleSolver import PuzzleSolver
from Checkerboard import Checkerboard

if __name__ == '__main__':
    # 解N皇后问题
    queen_num = int(input("请输入皇后个数："))
    puzzle_solver = PuzzleSolver(queen_num)
    puzzle_solver.solve(0)
    result = puzzle_solver.get_result()
    # 导出结果为表格
    checker_board = Checkerboard('test.xlsx')
    checker_board.play(result)
