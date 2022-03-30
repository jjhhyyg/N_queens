N = 0
# bool数组，判定哪些地方不能被占领，同时用于回溯
# 注意棋盘下标为0~n-1
place = None
col = None
diagonal = None
anti_diagonal = None


class PuzzleSolver:
    """求解N皇后问题的类"""

    def __init__(self, n):
        """
        :param n: 皇后个数（棋盘大小）
        """
        global N, place, col, diagonal, anti_diagonal
        N = n
        place = [0] * N
        col = [True] * N
        diagonal = [True] * (2 * N - 1)
        anti_diagonal = [True] * (2 * N - 1)

        # 存储结果
        self.result = []

    def solve(self, i):
        """
        求解N皇后问题，结果储存在self.result中
        :param i: 求第i行皇后位置
        :return: None
        """
        global N
        for j in range(N):
            # 判断是否可以在第i行第j列放置第i个皇后
            if col[j] and diagonal[i - j + N - 1] and anti_diagonal[i + j]:
                # 在第i行第col列放置皇后
                place[i] = j
                col[j] = False
                diagonal[i - j + N - 1] = False
                anti_diagonal[i + j] = False
                if i < N - 1:
                    # 求下一列的皇后位置
                    self.solve(i + 1)
                else:
                    self.result.append(place.copy())

                # 回溯
                col[j] = True
                diagonal[i - j + N - 1] = True
                anti_diagonal[i + j] = True

    def get_result(self):
        return self.result
