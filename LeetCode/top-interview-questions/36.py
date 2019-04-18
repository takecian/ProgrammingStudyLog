# https://leetcode.com/problems/valid-sudoku/

import itertools
from collections import Counter
import bisect


class Solution:
    def isValidSudoku(self, board):
        print(board)
        # check rows
        for i in range(9):
            digits = set()
            dot_count = 0
            for j in range(9):
                if board[i][j] != '.':
                    digits.add(board[i][j])
                else:
                    dot_count += 1
            if len(digits) != 9 - dot_count:
                return False

        # check colums
        for i in range(9):
            digits = set()
            dot_count = 0
            for j in range(9):
                if board[j][i] != '.':
                    digits.add(board[j][i])
                else:
                    dot_count += 1
            if len(digits) != 9 - dot_count:
                return False

        # check sub boxes
        for i in range(3):
            for j in range(3):
                digits = set()
                dot_count = 0
                for k in range(3):
                    for l in range(3):
                        if board[i * 3 + k][j * 3 + l] != '.':
                            digits.add(board[i * 3 + k][j * 3 + l])
                        else:
                            dot_count += 1
                if len(digits) != 9 - dot_count:
                    return False

        return True


def main():
    s = Solution()
    print(s.isValidSudoku([
                     ["8","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]
                    ]))

if __name__ == '__main__':
    main()
