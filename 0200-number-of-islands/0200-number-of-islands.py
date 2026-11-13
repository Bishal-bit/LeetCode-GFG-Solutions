class Solution:
    def isvalid(self, i: int, j: int, m:int, n:int) -> bool:
        #Checking if index is in vaid range or not
        return 0<= i< m and 0<= j< n
    def bfs(self, i: int, j: int, visited: List[List[str]], grid: List[List[str]], m:int, n:int) :
        #Mark visited of [i][j] as True
        visited[i][j]=True
        q=deque()           #Declare q to perform BFS
        q.append((i,j))     #Append indices to q
        while q :
            a, b=q.popleft()    #Pop the indices
            direction=[(-1,0), (1,0), (0,-1), (0,1)] #All 4 directions
            
            for row1, col1 in direction: #Check all 4 directions
                row=a+row1
                col=b+col1
                #If valid, grid value as 1, not visited then mark as visited, append to q
                if self.isvalid(row, col, m, n) and grid[row][col]=="1" and not visited[row][col] :
                    visited[row][col]=True
                    q.append((row, col))

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n=len(grid), len(grid[0])
        #Declare visited to keep track of visited indices
        visited=[[False for _ in range(n)] for _ in range(m)]
        count=0         #Count for storing no of islands
        
        for i in range(m) :
            for j in range(n) :
                #If not visited, grid value as 1 then it is an island. Increment count, run BFS
                if not visited[i][j] and grid[i][j]=="1" :
                    count+=1
                    self.bfs(i, j, visited, grid, m, n)
        #Return count            
        return count
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna