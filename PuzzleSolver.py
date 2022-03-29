class PuzzleSolver:
    """求解N皇后问题的类"""

    def __init__(self, n):
        """
        :param n: 皇后个数（棋盘大小）
        """

        self.N = n

        # bool数组，判定哪些地方不能被占领，同时用于回溯
        # 注意棋盘下标为0~n-1

        self.place = [0] * n
        self.col = [True] * n
        self.diagonal = [True] * (2 * n - 1)
        self.anti_diagonal = [True] * (2 * n - 1)

        # 存储结果
        self.result = []

    def solve(self, i):
        """
        求解N皇后问题，结果储存在self.result中
        :param i: 求第i行皇后位置
        :return: None
        """

        for j in range(self.N):
            # 判断是否可以在第i行第j列放置第i个皇后
            if self.col[j] and self.diagonal[i - j + self.N - 1] and self.anti_diagonal[i + j]:
                # 在第i行第col列放置皇后
                self.place[i] = j
                self.col[j] = False
                self.anti_diagonal[i + j] = False
                self.diagonal[i - j + self.N - 1] = False

                if i < self.N - 1:
                    # 求下一列的皇后位置
                    self.solve(i + 1)
                else:
                    self.result.append(self.place)
                    self.place = [0] * self.N

                # 回溯
                self.col[j] = True
                self.anti_diagonal[i + j] = True
                self.diagonal[i - j + self.N - 1] = True

    def get_result(self):
        return self.result
