
def numIslands(grid):

    def dfs(i,j):

        if (i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0):
            if (grid[i][j] == 1):
                grid[i][j] = 0
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i, j+1)
                dfs(i, j-1)
            else:
                return
        else:
            return

    islandCount = 0

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):

            if (grid[i][j] == 1):
                print(grid[i][j])
                islandCount += 1
                dfs(i,j)
    print(grid)
    
    return islandCount

if __name__ == "__main__":
    numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])