#!/usr/bin/python3
import sys

def is_valid(board, row, col):
    for i in range(col):
        if board[i] == row or \
            board[i] - i == row - col or \
            board[i] + i == row + col:
            return False
    return True

def solve_n_queens(board, col, n):
    if col == n:
        return [board[:]]
    
    solutions = []
    for i in range(n):
        if is_valid(board, i, col):
            board[col] = i
            for solution in solve_n_queens(board, col + 1, n):
                solutions.append(solution)
    return solutions

def nqueens(n):
    board = [-1] * n
    solutions = solve_n_queens(board, 0, n)
    for solution in solutions:
        print([list(p) for p in enumerate(solution)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
