class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            # Base case: If indices are out of bounds or the cell is not 'O', return
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return
            # Mark the cell as temporary 'T'
            board[r][c] = "T"
            # Recursive DFS to capture neighboring 'O' cells
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        # Step 2: Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Step 3: Uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"