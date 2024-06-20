def solveNQueens(N):
    def isSafe(board, row, col):
        # Check this column on the upper side
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the major diagonal on the upper side
        
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check the minor diagonal on the upper side
        for i, j in zip(range(row, -1, -1), range(col, N)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def solve(board, row):
        # Base case: If all queens are placed
        if row >= N:
            result.append(["".join(r) for r in board])
            return True
        
        res = False
        for col in range(N):
            if isSafe(board, row, col):
                board[row][col] = 'Q'
                res = solve(board, row + 1) or res
                board[row][col] = '.'
        
        return res

    # Initialize the board
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []
    solve(board, 0)
    return result

# Example usage:
N = 6 
solutions = solveNQueens(N)
for solution in solutions:
    for row in solution:
        print(row)
    print()
