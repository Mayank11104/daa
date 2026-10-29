
print("N-Queens Problem using Backtracking")

n = int(input("Enter number of queens: "))

if n <= 0:
    print("Enter a positive integer.")
else:
    board = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        # Check column in previous rows
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        # All queens are placed
        if row == n:
            return True

        # Try every column
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1

                if solve(row + 1):
                    return True

                # Backtrack
                board[row][col] = 0

        return False

    if solve(0):
        print("Solution:")
        for row in board:
            print(row)
    else:
        print("No solution exists for", n, "queens.")
