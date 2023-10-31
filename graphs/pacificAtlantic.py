def pacificAtlantic(heights):

    pacific = [[None] * len(heights[0])] * len(heights)
    atlantic = [[None] * len(heights[0])] * len(heights)
    visited = []

    def dfs(i, j):

        print ("DFS   " + str(i) + "  " + str(j))
        print(pacific)
        print(atlantic)     

        if (i < 0 or i >= len(heights) or j < 0 or j >= len(heights[0])):
            print("Invalid Indices")
            return (False, False)

        if ((i,j) in visited):
            print("This was visited: ")
            print("i: " + str(i) + " j: " + str(j) + "  " + str(pacific[i][j]))
            print("i: " + str(i) + " j: " + str(j) + "  " + str(atlantic[i][j]))
            return (pacific[i], atlantic[j])
        else:
            
            visited.append((i,j))

        print("VISITED: ")
        print(visited)


        if (i == 0 or j == 0):
            print("====")
            print(pacific[i])
            print(pacific[i][j])
            pacific[i][j] = True
            print(pacific)
            print("====")

        if (i == (len(heights) - 1) or j == (len(heights[0]) - 1)):
            atlantic[i][j] = True


        if (pacific[i][j] == None or atlantic[i][j] == None):
            
            (a, b) = dfs(i+1, j)
            (c, d) = dfs(i-1, j)
            (e, f) = dfs(i, j+1)
            (g, h) = dfs(i, j-1)


            if (((a == True) and (heights[i][j] >= heights[i+1][j])) or 
                ((c == True) and (heights[i][j] >= heights[i-1][j])) or 
                ((e == True) and (heights[i][j] >= heights[i][j+1])) or 
                ((g == True) and (heights[i][j] >= heights[i][j-1]))):

                pacific[i][j] = True
                
            else:
                pacific[i][j] = False

            

            if (((b == True) and (heights[i][j] >= heights[i+1][j])) or 
                ((d == True) and (heights[i][j] >= heights[i-1][j])) or 
                ((f == True) and (heights[i][j] >= heights[i][j+1])) or 
                ((h == True) and (heights[i][j] >= heights[i][j-1]))):
                atlantic[i][j] = True

            else:
                pacific[i][j] = False


        print("i: " + str(i) + " j: " + str(j) + "  " + str(pacific[i][j]))
        print("i: " + str(i) + " j: " + str(j) + "  " + str(atlantic[i][j]))

        return (pacific[i][j],atlantic[i][j])

    
    for i in range(0, len(heights)):
        for j in range(0, len(heights[0])):
            if (pacific[i][j] == None and atlantic[i][j] == None):
                dfs(i, j)

    print(pacific)
    print(atlantic)              

    result = []
    for i in range(0, len(heights)):
        for j in range(0, len(heights[0])):
            if (pacific[i][j] == True and atlantic[i][j] == True):
                result.append([i, j])


    return result

if __name__ == "__main__":
    pacificAtlantic([[1,2],[3,2]])
