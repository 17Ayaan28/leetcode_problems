class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])
        visited = []
        Ncaptured = []

        def dfs(i, j):
            if (i < 0 or i == ROWS or j < 0 or j == COLS or board[i][j] == "X"):
                return
            visited.append((i, j))
            if ((i+1, j) not in visited): dfs(i+1, j)
            if ((i-1, j) not in visited): dfs(i-1, j)
            if ((i, j+1) not in visited): dfs(i, j+1)
            if ((i, j-1) not in visited): dfs(i, j-1)



        for j in range(0, COLS):
            if (board[0][j] == "O" and ((0, j) not in visited)):
                dfs(0, j)
            
            if (board[ROWS-1][j] == "O" and ((ROWS-1, j) not in visited)):
                dfs(ROWS-1, j)

        for i in range(0, ROWS):
            if (board[i][0] == "O" and ((i, 0) not in visited)):
                dfs(i, 0)
            
            if (board[i][COLS-1] == "O" and ((i, COLS-1) not in visited)):
                dfs(i, COLS-1)

        for i in range(0, ROWS):
            for j in range(0, COLS):
                if ((i,j) not in visited):
                    board[i][j] = "X"
                
        
        