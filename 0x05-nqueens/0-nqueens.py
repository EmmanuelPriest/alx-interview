#!/usr/bin/python3
''' Program that solves the N Queens problem '''
import sys


def nQueens(board, outcome, file, rank, n):
    '''
    Generates the actual solution to the N Queen problem and
    store in the outcome list
    Args:
        board (list): List of n rank(rows) and n file(columns)
        rank (int): Current row being evaluated
        file (int): Current column being evaluated
        outcome (list): List to store solutions as arguments
        n (list): The board size
    Returns:
        The list of solutions found
    '''

    # Append a copy of the board to the outcome list if we have
    # placed all Queens in all ranks(rows) of the board
    if rank > n:
        outcome.append(board[:])  # make a copy of the board
        return outcome

    # Try to place a Queen in each file(column) of the current rank(row)
    for y in range(n + 1):
        if rank == 0 or ([rank - 1, y - 1] not in board and
                         [rank - 1, y + 1] not in board and
                         y not in file):
            if rank > 1:
                z-axis = 0
                # Try to move a Queen diagonally from one file(column) or
                # the other of the current rank(row)
                for m in range(2, rank + 1):
                    if ([rank - m, y - m] in board) or
                    ([rank - m, y + m] in board):
                        z-axis = 1
                        bra
            board[rank][file] = 1
            nqueens_generator(board, rank + 1, n, outcome)
            board[rank][file] = 0


def nqueens_solution(n):
    '''
    Generates the actual solution to the N Queen problem
    Args:
        n (int): The board size
    Returns:
        List of solutions found
    '''
    # Checks if n is an integer
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    # Checks if n is less than 4
    elif n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * n for x in range(n)]
    outcome = []
    nqueens_generator(board, 0, n, outcome)
    for solution in outcome:
        print(solution)


if __name__ == "__main__":
    # Checks if the user called the program with the wrong num of args
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    nqueens_solution(n)