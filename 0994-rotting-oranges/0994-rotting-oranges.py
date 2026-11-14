class Solution:
    def isvalid(self,i: int, j:int, m: int, n:int) :
        return 0<=i<m and 0<=j<n
    def bfs(self, q, time: int, m: int, n:int, grid: list[list[int]]) :
        #If q is empty then return q
        if not q : return time
        n1=len(q)       #Length of q
        for i in range(n1) :
            a, b, t=q.popleft()
            time=max(time, t)   #Update time
            
            directions=[[-1,0], [1,0], [0,-1], [0,1]]
            for it in directions :
                row=a+it[0]
                col=b+it[1]
                
                #Valid and fresh
                if self.isvalid(row, col, m, n) and grid[row][col]==1 :
                    grid[row][col]=2            #Make it rotten
                    q.append((row, col, t+1))   #Append to q by adding 1 to t
                    time=max(time, t+1)         #Update time
            #Return BFS
            return self.bfs(q, time, m, n, grid)

    def orangesRotting(self, grid: list[list[int]]) -> int:
        #BFS
        m, n= len(grid), len(grid[0])
        count=0
        q=deque()
        for i in range(m) :
            for j in range(n) :
                #If rotten then append to q
                if grid[i][j]==2 : q.append((i,j,0))
        
        #Call BFS
        time=self.bfs(q, 0, m, n, grid)
        #Check if any fresh orange is left or not
        for i in range(m) :
            for j in range(n) :
                if grid[i][j]==1 : return -1
        
        #Return time
        return time


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna